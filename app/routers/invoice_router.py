# invoice_service/app/routers/invoices.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.invoice_schema import InvoiceCreate, Invoice
from app.schemas.base_schema import ResponseWithMessage
from app.services.invoice_services import create_new_invoice, get_single_invoice
from app.dependencies import get_db
from uuid import UUID

router = APIRouter()

@router.post("/", response_model=ResponseWithMessage)
def create_invoice(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    create_new_invoice(db, invoice)
    return {"status":True,"message": "Your invoice has been created successfully."}

@router.get("/{invoice_uuid}", response_model=Invoice)
def read_invoice(invoice_uuid: str, db: Session = Depends(get_db)):
    db_invoice = get_single_invoice(db, invoice_uuid)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice
