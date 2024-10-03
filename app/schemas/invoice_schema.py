from pydantic import BaseModel
from datetime import datetime
from typing import Any


class InvoiceCreate(BaseModel):
    order_id: str
    total_amount: float
    details: Any  # Sipariş detaylarını içeriyor

class Invoice(BaseModel):
    invoice_uuid: str
    order_id: str
    invoice_date: datetime
    total_amount: float
    details: Any

    class Config:
        orm_mode = True
