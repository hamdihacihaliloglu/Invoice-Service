# invoice_service/app/services/invoice_service.py
from sqlalchemy.orm import Session
from app.repositories import invoice_repository
from app.schemas.invoice_schema import InvoiceCreate

def create_new_invoice(db: Session, invoice: InvoiceCreate):
    return invoice_repository.create_invoice(db, invoice)

def get_single_invoice(db: Session, invoice_uuid):
    return invoice_repository.get_invoice(db, invoice_uuid)
