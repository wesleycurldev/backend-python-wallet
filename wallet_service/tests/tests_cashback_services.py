import sys
import unittest

from mocks.cashback_services_mocks import cashback_data 

sys.path.append('..')
sys.path.append('../..')

from domain.cashbacks.entities import Cashback
from domain.cashbacks.exceptions import (
    InvalidCustomerDocument,
    InvalidProductType,
    InvalidSoldAt
)
from application.cashback.cashback_services import CashbackService
from application.cashback.cashback_dto import CashbackDto
from application.cashback.cashback_storage import CashbackStorage


class DummyStorage(CashbackStorage):
    def save_cashback(self, cashback_dto: CashbackDto):
        return True


class CashbackTests(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        self.dummy_storage = DummyStorage()
        super().__init__(methodName)
    
    def test_customer_document_should_be_valid(self):
        data = cashback_data()
        data["customer"]["document"] = "864.466.290-286"

        cashback = Cashback(
            sold_at=data["sold_at"], 
            customer=data["customer"], 
            total=data["total"], 
            products=data["products"]
        )
        self.assertRaises(InvalidCustomerDocument, cashback.is_valid)
        
    def test_product_type_should_be_valid(self):
        data = cashback_data()
        data["products"][0]["type"] = "H"

        cashback = Cashback(
            sold_at=data["sold_at"], 
            customer=data["customer"], 
            total=data["total"], 
            products=data["products"]
        )
        self.assertRaises(InvalidProductType, cashback.is_valid)

    def test_sold_at_should_be_valid(self):
        data = cashback_data()
        data["sold_at"] = "2020-01-01"

        cashback = Cashback(
            sold_at=data["sold_at"], 
            customer=data["customer"], 
            total=data["total"], 
            products=data["products"]
        )
        self.assertRaises(InvalidSoldAt, cashback.is_valid)

    def test_the_sum_of_the_value_of_products(self):
        data = cashback_data()
        
        cashback = Cashback(
            sold_at=data["sold_at"], 
            customer=data["customer"], 
            total=data["total"], 
            products=data["products"]
        )
        sum_value_products = sum(float(item['value']) for item in cashback.products)
        self.assertEqual(sum_value_products, 100.0)

    def test_create_new_cashback(self):
        data = cashback_data()

        cashback_dto = CashbackDto(
            sold_at=data["sold_at"], customer=data["customer"], total=data["total"], products=data["products"])
        service = CashbackService(storage=self.dummy_storage)
        res = service.create_new_cashback(cashback_dto)

        self.assertEqual(res['code'], 'SUCCESS')


if __name__ == '__main__':
    unittest.main()
