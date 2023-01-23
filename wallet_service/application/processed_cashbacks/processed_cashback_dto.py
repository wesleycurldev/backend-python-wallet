import uuid

from datetime import datetime

from wallet_service.domain.processed_cashbacks.entities import ProcessedCashback

# ProcessedCashbackDto tem a responsabilidade de transportar dados de uma camada para a outra.
class ProcessedCashbackDto(object):
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


    def to_domain(self):
        return ProcessedCashback(self.cashback_id, self.created_at, self.message, self.cashback_reference_id, self.document, self.cashback)

    def to_dto(self, processed_cashback: ProcessedCashback):
        processed_cashback_dto = ProcessedCashbackDto(
            cashback=processed_cashback.cashback,
            cashback_id=processed_cashback.cashback_id,
            cashback_reference_id=processed_cashback.cashback_reference_id,
            created_at=processed_cashback.created_at,
            document=processed_cashback.document,
            message=processed_cashback.message
        )
        return processed_cashback_dto