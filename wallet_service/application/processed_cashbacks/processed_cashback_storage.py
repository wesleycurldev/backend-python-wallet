from abc import ABC, abstractclassmethod
from .processed_cashback_dto import ProcessedCashbackDto

class ProcessedCashbackStorage(ABC):
    
    @abstractclassmethod
    def save_processed_cashback(self, processed_cashback_dto: ProcessedCashbackDto):
        pass