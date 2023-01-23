from flask import Flask, request
from flask_cors import CORS
from models.db import db

from repositories.cashbacks import CashbackRepository, CashbackDto, CashbackService
from repositories.processed_cashbacks import ProcessedCashbackRepository, ProcessedCashbackDto, ProcessedCashbackService
from external_requests.confirm_cashback import confirm_cashback

from dotenv import load_dotenv
from os import environ

load_dotenv()

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "http://localhost:5000"}})

app.config['SECRET_KEY'] = environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.app_context().push()


@app.route('/api/cashback', methods=['POST'])
def cashback():
    try:
        request_body = request.get_json()
        
        cashback_repository = CashbackRepository()
        cashback_service = CashbackService(cashback_repository)
        cashback_dto = CashbackDto(
            sold_at=request_body['sold_at'],
            customer=request_body['customer'],
            total=request_body['total'],
            products=request_body['products']
        )

        cashback_response = cashback_service.create_new_cashback(cashback_dto=cashback_dto)
     
        # verifica se o retorno do create_new_cashback tem algum erro
        if cashback_response['code'] != 'SUCCESS':
            return { 'message': cashback_response['message'], 'code': cashback_response['code'].value, 'error': True }
        
        confirm_cashback_response = confirm_cashback(
            document=cashback_response['data'].customer['document'],
            cashback_value=cashback_response['data'].total
        )
        
        # verifica se o retorno do confirm_cashback (requisição externa) tem algum erro
        if confirm_cashback_response['code'] != 'SUCCESS':
            return { 'message': confirm_cashback_response['message'], 'code': confirm_cashback_response['code'], 'error': True }
        
        processed_cashback_repository = ProcessedCashbackRepository()
        processed_cashback_service = ProcessedCashbackService(processed_cashback_repository)
        processed_cashback_dto = ProcessedCashbackDto(
            cashback=confirm_cashback_response['data']['cashback'],
            cashback_id=cashback_response['data'].id,
            cashback_reference_id=confirm_cashback_response['data']['id'],
            created_at=confirm_cashback_response['data']['createdAt'],
            document=confirm_cashback_response['data']['document'],
            message=confirm_cashback_response['data']['message']
        )

        processed_cashback_response = processed_cashback_service.create_new_processed_cashback(processed_cashback_dto)
        # verifica se o retorno do create_new_processed_cashback tem algum erro
        if processed_cashback_response['code'] != 'SUCCESS':
            return { 'message': processed_cashback_response['message'], 'code': processed_cashback_response['code'], 'error': True }
        
        return { 'message': processed_cashback_response['message'], 'code': processed_cashback_response['code'], 'error': False }
    except Exception as e:
        return {'message': str(e), 'error': True}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)