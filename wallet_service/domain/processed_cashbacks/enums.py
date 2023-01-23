from enum import Enum

class ErrorCodes(Enum):
    PROCESSED_CASHBACK_ERROR = "PROCESSED_CASHBACK_ERROR"
    INVALID_CREATED_AT = "INVALID_CREATED_AT"
    INVALID_DOCUMENT = "INVALID_DOCUMENT"
    UNDEFINED_ERROR = "UNDEFINED_ERROR"
    
class SuccessCodes(Enum):
    SUCCESS = 'SUCCESS'
