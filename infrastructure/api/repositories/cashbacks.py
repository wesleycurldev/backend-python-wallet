import sys

sys.path.append('..')
sys.path.append('../..')

from wallet_service.application.cashback.cashback_storage import CashbackStorage
from wallet_service.application.cashback.cashback_dto import CashbackDto
from wallet_service.application.cashback.cashback_services import CashbackService
from models.cashbacks import Cashbacks
from models.db import db

class CashbackRepository(CashbackStorage):
    def __init__(self):
        self.db = db
    
    def save_cashback(self, cashback_dto: CashbackDto):
        cashback = Cashbacks(
            customer=cashback_dto.customer,
            products=cashback_dto.products,
            sold_at=cashback_dto.sold_at,
            total=cashback_dto.total
        )
        
        self.db.session.add(cashback)
        self.db.session.commit()
        return cashback