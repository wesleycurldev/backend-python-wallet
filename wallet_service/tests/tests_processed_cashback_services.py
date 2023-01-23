import sys
import unittest
import uuid

from mocks.processed_cashback_services_mocks import processed_cashback_data 

sys.path.append('..')
sys.path.append('../..')

from domain.processed_cashbacks.entities import ProcessedCashback
from domain.processed_cashbacks.exceptions import (
    InvalidDocument,
    InvalidCreatedAt
)
from application.processed_cashbacks.processed_cashback_services import ProcessedCashbackService
from application.processed_cashbacks.processed_cashback_dto import ProcessedCashbackDto
from application.processed_cashbacks.processed_cashback_storage import ProcessedCashbackStorage


class DummyStorage(ProcessedCashbackStorage):
    def save_processed_cashback(self, processed_cashback_dto: ProcessedCashbackDto):
        return True

class ProcessedCashbackTests(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        self.dummy_storage = DummyStorage()
        super().__init__(methodName)
    
    def test_sold_at_should_be_valid(self):
        data = processed_cashback_data()
        data["document"] = "335353535359"

        processed_cashback = ProcessedCashback(
            cashback_id=uuid.uuid4(), 
            created_at=data["createdAt"], 
            message=data["message"], 
            cashback_reference_id=data["id"],
            document=data["document"],
            cashback=data["cashback"]
        )
        self.assertRaises(InvalidDocument, processed_cashback.is_valid)
            
    def test_customer_document_should_be_valid(self):
        data = processed_cashback_data()
        data["createdAt"] = "2023-01-50T23:36:44.646Z6"

        processed_cashback = ProcessedCashback(
            cashback_id=uuid.uuid4(), 
            created_at=data["createdAt"], 
            message=data["message"], 
            cashback_reference_id=data["id"],
            document=data["document"],
            cashback=data["cashback"]
        )
        self.assertRaises(InvalidCreatedAt, processed_cashback.is_valid)
    
    def test_create_new_processed_cashback(self):
        data = processed_cashback_data()

        processed_cashback_dto = ProcessedCashbackDto(
            cashback_id=uuid.uuid4(), 
            created_at=data["createdAt"], 
            message=data["message"], 
            cashback_reference_id=data["id"],
            document=data["document"],
            cashback=data["cashback"]
        )
        service = ProcessedCashbackService(storage=self.dummy_storage)
        res = service.create_new_processed_cashback(processed_cashback_dto)

        self.assertEqual(res['code'], 'SUCCESS')


if __name__ == '__main__':
    unittest.main()
