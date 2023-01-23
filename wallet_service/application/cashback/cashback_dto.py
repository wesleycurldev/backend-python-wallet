from datetime import datetime

from wallet_service.domain.cashbacks.entities import Cashback

# CashbackDto tem a responsabilidade de transportar dados de uma camada para a outra.
class CashbackDto(object):
    sold_at: datetime
    customer: dict
    total: float
    products: list

    def __init__(self, sold_at: datetime, customer: dict, total: float, products: list):
        self.sold_at = sold_at
        self.customer = customer
        self.total = total
        self.products = products

    def to_domain(self):
        return Cashback(self.sold_at, self.customer, self.total, self.products)
    
    def to_dto(self, cashback: Cashback):
        cashback_dto = CashbackDto(
            customer=cashback.customer,
            products=cashback.products,
            sold_at=cashback.sold_at,
            total=cashback.total
        )
        return cashback_dto
