import re

from datetime import datetime
from .exceptions import InvalidCustomerDocument, InvalidProductType, InvalidSoldAt, InvalidTotal, CashbackError

# Caso não seja válido é levantado uma custom exeception onde eu trato na camada de use_case (cashback_service).
# Isso é importante para que não seja enviada nenhuma mensagem que eu não queira que saia do meu dominio.

class Cashback(object):
    sold_at: datetime
    customer: dict
    total: float
    products: list

    def __init__(self, sold_at: datetime, customer: dict, total: float, products: list):
        self.sold_at = sold_at
        self.customer = customer
        self.total = total
        self.products = products

    def create_cashback(self):
        self.total = round(float(self.total), 1)        
        self.is_valid()

        self.sold_at = self.convert_to_timestamp(self.sold_at)

    def convert_to_timestamp(self, obj_datetime):
        return datetime.strptime(obj_datetime,'%Y-%m-%d %H:%M:%S').isoformat()

    def is_valid(self):
        try:
            # valida se o cpf é válido com uma regex para ambos os formatos (864.466.290-28, 86446629028).
            document_expr = re.compile('^(([0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2})|([0-9]{11}))$')
            if not document_expr.search(self.customer["document"]):
                raise InvalidCustomerDocument("Invalid document")
            
            # valida se o type é um valor permitido.
            if False in [True if product["type"] in ["A", "B", "C"] else False for product in self.products]:
                raise InvalidProductType("Type is not among the allowed values: A, B, C")

            # valida se o sold_at é uma data com o formato válido (%Y-%m-%d %H:%M:%S).
            sold_at_expr = re.compile('[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]')
            if not sold_at_expr.search(self.sold_at):
                raise InvalidSoldAt("Invalid sold_at")
            
            # valida se o total é igual a soma dos valores dos produtos
            sum_value_products = round(sum(float(item['value']) for item in self.products),1)
            if sum_value_products != self.total:
                raise InvalidTotal("Invalid total")
            
            return True
        except ValueError as e:
            raise CashbackError(e)