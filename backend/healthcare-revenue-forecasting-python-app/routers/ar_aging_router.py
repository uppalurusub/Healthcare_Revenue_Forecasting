from fastapi import APIRouter

from services.ar_aging_service import (
    ARAgingService
)

router = APIRouter()

ar_service = ARAgingService()


# ==========================================
# AR Summary
# ==========================================

@router.get("/summary")
def ar_summary():

    return (
        ar_service
        .ar_summary()
    )


# ==========================================
# AR Trend
# ==========================================

@router.get("/trend")
def ar_trend():

    return (
        ar_service
        .ar_trend()
    )


# ==========================================
# Monthly AR Trend
# ==========================================

@router.get("/monthly")
def monthly_ar():

    return (
        ar_service
        .monthly_ar()
    )


# ==========================================
# Aging Buckets
# ==========================================

@router.get("/aging-buckets")
def aging_buckets():

    return (
        ar_service
        .aging_bucket_analysis()
    )


# ==========================================
# Collection Status
# ==========================================

@router.get("/collection-status")
def collection_status():

    return (
        ar_service
        .collection_status_analysis()
    )


# ==========================================
# Risk Analysis
# ==========================================

@router.get("/risk-analysis")
def risk_analysis():

    return (
        ar_service
        .risk_analysis()
    )


# ==========================================
# Payer Analysis
# ==========================================

@router.get("/payer")
def payer_analysis():

    return (
        ar_service
        .payer_analysis()
    )


# ==========================================
# Department Analysis
# ==========================================

@router.get("/department")
def department_analysis():

    return (
        ar_service
        .department_analysis()
    )


# ==========================================
# Expected Collections
# ==========================================

@router.get("/expected-collections")
def expected_collections():

    return (
        ar_service
        .expected_collections()
    )


# ==========================================
# High Risk Accounts
# ==========================================

@router.get("/high-risk")
def high_risk_accounts():

    return (
        ar_service
        .high_risk_accounts()
    )


# ==========================================
# Top Payers
# ==========================================

@router.get("/top-payers")
def top_payers(
        top_n: int = 10
):

    return (
        ar_service
        .top_payers(top_n)
    )


# ==========================================
# AR KPIs
# ==========================================

@router.get("/kpis")
def ar_kpis():

    return (
        ar_service
        .ar_kpis()
    )