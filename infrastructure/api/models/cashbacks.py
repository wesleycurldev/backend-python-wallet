import uuid
from .db import db
from sqlalchemy.dialects.postgresql import UUID, JSONB


class Cashbacks(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sold_at = db.Column(db.DateTime(timezone=True))
    customer = db.Column(JSONB)
    total = db.Column(db.Float)
    products = db.Column(JSONB)

    def __init__(self, customer, sold_at, total, products):
        self.customer = customer
        self.sold_at = sold_at
        self.total = total
        self.products = products