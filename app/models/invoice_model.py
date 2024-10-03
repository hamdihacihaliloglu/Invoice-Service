# invoice_service/app/models/invoice.py
from sqlalchemy import Column, String, DECIMAL, DateTime, Integer
from sqlalchemy.dialects.mysql import BINARY
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from app.models.base_model import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_uuid = Column(String(36), unique=True,nullable=False)
    order_id = Column(String(36), nullable=False, unique=True)
    invoice_date = Column(DateTime, default=datetime.now)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    details = Column(String(1000), nullable=False)  # JSON string olarak saklanabilir

