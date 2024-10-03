# invoice_service/app/repositories/invoice_repository.py
from sqlalchemy.orm import Session
from app.models.invoice_model import Invoice
from app.schemas.invoice_schema import InvoiceCreate
import uuid

def create_invoice(db: Session, invoice: InvoiceCreate):
    try:
        db_invoice = Invoice(
            invoice_uuid=str(uuid.uuid4()),
            order_id=invoice.order_id,
            total_amount=invoice.total_amount,
            details=str(invoice.details)
        )
        db.add(db_invoice)
        db.commit()
        db.refresh(db_invoice)
        return db_invoice
    except Exception as e:
        db.rollback()  # Hata durumunda işlemi geri alır
        print(f"An error occurred while creating the invoice: {e}")
        raise Exception("We encountered an issue while creating your invoice. Please try again or contact our support team if the issue persists.")



def get_invoice(db: Session, invoice_uuid: str):
    return db.query(Invoice).filter(Invoice.invoice_uuid == invoice_uuid).first()
