class ProcessedCashbackError(Exception):
    def __init__(self, message):
        self.message = message
        
class InvalidCreatedAt(Exception):
    def __init__(self, message):
        self.message = message

class InvalidDocument(Exception):
    def __init__(self, message):
        self.message = message