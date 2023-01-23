import uuid
from .db import db
from sqlalchemy.dialects.postgresql import UUID


class ProcessedCashbacks(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cashback_id = db.Column(UUID(as_uuid=True))
    created_at = db.Column(db.DateTime(timezone=True))
    message = db.Column(db.String)
    cashback_reference_id = db.Column(db.Integer)
    document = db.Column(db.String)
    cashback = db.Column(db.Float)

    def __init__(self, cashback_id, created_at, message, cashback_reference_id, document, cashback):
        self.cashback_id = cashback_id
        self.created_at = created_at
        self.message = message
        self.cashback_reference_id = cashback_reference_id
        self.document = document
        self.cashback = cashback
