import re
import uuid

from datetime import datetime
from .exceptions import ProcessedCashbackError, InvalidCreatedAt, InvalidDocument

# Caso não seja válido é levantado uma custom exeception onde eu trato na camada de use_case (cashback_service).
# Isso é importante para que não seja enviada nenhuma mensagem que eu não queira expor fora do meu dominio.

class ProcessedCashback(object):
    cashback_id: uuid
    created_at: datetime
    message: str
    cashback_reference_id: int
    document: str
    cashback: float

    def __init__(self, cashback_id: uuid, created_at: datetime, message: str, cashback_reference_id: int, document: str, cashback: float):
        self.cashback_id = cashback_id
        self.created_at = created_at
        self.message = message
        self.cashback_reference_id = cashback_reference_id
        self.document = document
        self.cashback = cashback

    def create_processed_cashback(self): 
        self.is_valid()
        
        self.created_at = self.convert_to_timestamp(self.created_at) 
      
        

    def convert_to_timestamp(self, obj_datetime):
        return datetime.strptime(obj_datetime,'%Y-%m-%dT%H:%M:%S.%f%z').isoformat()

    def is_valid(self):
        try:
            # valida se o created_at é uma data com o formato válido (YYYY-MM-DDTHH:MM:SS.000).
            created_at_expr = re.compile('^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z)$')
            if not created_at_expr.search(self.created_at):
                raise InvalidCreatedAt("Invalid created_at")
            
            # valida se o cpf é válido com uma regex para ambos os formatos (864.466.290-28, 86446629028).
            document_expr = re.compile('^(([0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2})|([0-9]{11}))$')
            if not document_expr.search(self.document):
                raise InvalidDocument("Invalid document")
            
            return True
        except ValueError as e:
            raise ProcessedCashbackError(e)
