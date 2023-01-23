from wallet_service.application.cashback.cashback_dto import CashbackDto
from wallet_service.application.cashback.cashback_storage import CashbackStorage

from wallet_service.domain.cashbacks.exceptions import  (
    InvalidCustomerDocument, 
    InvalidProductType, 
    InvalidSoldAt,
    InvalidTotal, 
    CashbackError
) 
from wallet_service.domain.cashbacks.enums import ErrorCodes, SuccessCodes


class CashbackService(object):
    storage: CashbackStorage

    def __init__(self, storage: CashbackStorage) -> None:
        self.storage = storage
    
    def create_new_cashback(self, cashback_dto: CashbackDto):
        domain_object = cashback_dto.to_domain()

        try:
            domain_object.create_cashback()
            final_dto = cashback_dto.to_dto(domain_object)
            cashback = self.storage.save_cashback(final_dto)
            
            return {
                'message': SuccessCodes.SUCCESS.value, 
                'code': SuccessCodes.SUCCESS.name,
                'data': cashback
            }
        except InvalidCustomerDocument as e:
            return {'message': e.message, 'code': ErrorCodes.INVALID_CUSTOMER_DOCUMENT}
        except InvalidProductType as e:
            return {'message': e.message, 'code': ErrorCodes.INVALID_PRODUCT_TYPE}
        except InvalidSoldAt as e:
            return {'message': e.message, 'code': ErrorCodes.INVALID_SOLD_AT}
        except InvalidTotal as e:
            return {'message': e.message, 'code': ErrorCodes.INVALID_TOTAL}
        except CashbackError as e:
            return {'message': e.message, 'code': ErrorCodes.CASHBACK_ERROR}
        except Exception as e:
            return {'message': str(e), 'code': ErrorCodes.UNDEFINED_ERROR}
