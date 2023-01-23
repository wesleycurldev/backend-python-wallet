import sys

sys.path.append('..')
sys.path.append('../..')

from wallet_service.application.processed_cashbacks.processed_cashback_storage import ProcessedCashbackStorage
from wallet_service.application.processed_cashbacks.processed_cashback_dto import ProcessedCashbackDto
from wallet_service.application.processed_cashbacks.processed_cashback_services import ProcessedCashbackService
from models.processed_cashbacks import ProcessedCashbacks
from models.db import db

class ProcessedCashbackRepository(ProcessedCashbackStorage):
    def __init__(self):
        self.db = db
    
    def save_processed_cashback(self, processed_cashback_dto: ProcessedCashbackDto):
        processed_cashback = ProcessedCashbacks(
            cashback=processed_cashback_dto.cashback,
            cashback_id=processed_cashback_dto.cashback_id,
            cashback_reference_id=processed_cashback_dto.cashback_reference_id,
            created_at=processed_cashback_dto.created_at,
            document=processed_cashback_dto.document,
            message=processed_cashback_dto.message
        )
        
        self.db.session.add(processed_cashback)
        self.db.session.commit()
        return processed_cashback