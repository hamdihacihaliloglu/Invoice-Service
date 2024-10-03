from fastapi import FastAPI, status
from app.routers import invoice_router

app = FastAPI(
    title='Case Study Invoice Module',
    version='0.0.0.1',
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    docs_url="/api/v1/invoice-module/docs",
    openapi_url="/api/v1/invoice-module/openapi.json",
    redoc_url="/api/v1/invoice-module/redoc"
)

app.include_router(invoice_router.router, prefix="/api/v1/invoices", tags=["invoice"])