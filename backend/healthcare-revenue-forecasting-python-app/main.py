from fastapi import FastAPI

# Revenue
from routers.revenue_router import router as revenue_router


# Claims
from routers.claims_router import router as claims_router

# Payments
from routers.payments_router import router as payments_router

# Denials
from routers.denials_router import router as denials_router

# AR Aging
from routers.ar_aging_router import router as ar_aging_router

# Patient Billing
from routers.patient_billing_router import router as patient_billing_router


# Forecasting
from routers.forecasting_router import router as forecasting_router

# Dashboard
from routers.dashboard_router import router as dashboard_router


app = FastAPI(
    title="Healthcare Revenue Forecasting API",
    description="""
    End-to-End Healthcare Revenue Cycle Analytics

    Modules:
    - Revenue Analytics
    - Claims Analytics
    - Payments Analytics
    - Denial Analytics
    - AR Aging Analytics
    - Patient Billing Analytics
    - Revenue Forecasting
    - Executive Dashboard
    """,
    version="1.0.0"
)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Healthcare Revenue Cycle Analytics API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================
# Register Routers
# =====================================================

app.include_router(
    revenue_router,
    prefix="/api/revenue",
    tags=["Revenue"]
)


app.include_router(
    claims_router,
    prefix="/api/claims",
    tags=["Claims"]
)


app.include_router(
    payments_router,
    prefix="/api/payments",
    tags=["Payments"]
)

app.include_router(
    denials_router,
    prefix="/api/denials",
    tags=["Denials"]
)

app.include_router(
    ar_aging_router,
    prefix="/api/ar-aging",
    tags=["AR Aging"]
)


app.include_router(
    patient_billing_router,
    prefix="/api/patient-billing",
    tags=["Patient Billing"]
)


app.include_router(
    forecasting_router,
    prefix="/api/forecasting",
    tags=["Forecasting"]
)


app.include_router(
    dashboard_router,
    prefix="/api/dashboard",
    tags=["Executive Dashboard"]
)


# =====================================================
# Health Check
# =====================================================

@app.get("/")
def home():
    return {
        "application": "Healthcare Revenue Forecasting API",
        "status": "Running",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }