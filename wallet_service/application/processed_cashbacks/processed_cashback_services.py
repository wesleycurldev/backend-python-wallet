from wallet_service.application.processed_cashbacks.processed_cashback_dto import ProcessedCashbackDto
from wallet_service.domain.processed_cashbacks.exceptions import ProcessedCashbackError, InvalidCreatedAt, InvalidDocument
from wallet_service.domain.processed_cashbacks.enums import ErrorCodes, SuccessCodes
from wallet_service.application.processed_cashbacks.processed_cashback_storage import ProcessedCashbackStorage


class ProcessedCashbackService(object):
    storage: ProcessedCashbackStorage

    def __init__(self, storage: ProcessedCashbackStorage) -> None:
        self.storage = storage
    
    def create_new_processed_cashback(self, processed_cashback_dto: ProcessedCashbackDto):
        domain_object = processed_cashback_dto.to_domain()

        try:
            domain_object.create_processed_cashback()
            final_dto = processed_cashback_dto.to_dto(domain_object)
            processed_cashback = self.storage.save_processed_cashback(final_dto)

            return {
                'message': SuccessCodes.SUCCESS.value, 
                'code': SuccessCodes.SUCCESS.name,
                'data': processed_cashback
            }
        except ProcessedCashbackError as e:
            return {'message': e.message, 'code': ErrorCodes.PROCESSED_CASHBACK_ERROR}
        except InvalidCreatedAt as e:
            return {'message': e.message, 'code': ErrorCodes.INVALID_CREATED_AT}
        except InvalidDocument as e:
            return {'message': e.message, 'code': ErrorCodes.INVALID_DOCUMENT}
        except Exception as e:
            return {'message': str(e), 'code': ErrorCodes.UNDEFINED_ERROR}
