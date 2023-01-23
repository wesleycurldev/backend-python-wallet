from abc import ABC, abstractclassmethod
from .cashback_dto import CashbackDto

class CashbackStorage(ABC):
    
    @abstractclassmethod
    def save_cashback(self, cashback_dto: CashbackDto):
        pass