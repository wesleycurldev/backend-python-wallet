import requests
import json

from dotenv import load_dotenv
from os import environ

load_dotenv()


def confirm_cashback(document: str, cashback_value: float):
    try:
        # obs deixei comentado por que no presente momento a api não se encontrava funcionando!
        
        # payload = json.dumps({
        #     "document": document,
        #     "cashback": cashback_value
        # })
        # headers = {
        #     'Content-Type': 'application/json'
        # }

        # response = requests.request("POST", environ.get("CONFIRM_CASHBACK_URL"), headers=headers, data=payload)
   
        mock = {
            "createdAt": "2023-01-19T23:36:44.646Z",
            "message": "Cashback criado com sucesso!",
            "id": "96",
            "document": document,
            "cashback": cashback_value
        }
        
        return {
            'message': 'Sucess',
            'code': 'SUCCESS',
            'data': mock
        }
    except Exception as e:
        return {'message': str(e), 'code': 'EXTERNAL_REQUEST_ERROR', 'error': True}
