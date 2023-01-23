class InvalidCustomerDocument(Exception):
    def __init__(self, message):
        self.message = message

class InvalidProductType(Exception):
    def __init__(self, message):
        self.message = message

class InvalidSoldAt(Exception):
    def __init__(self, message):
        self.message = message


class InvalidTotal(Exception):
    def __init__(self, message):
        self.message = message

class CashbackError(Exception):
    def __init__(self, message):
        self.message = message
