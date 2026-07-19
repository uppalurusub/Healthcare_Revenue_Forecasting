from fastapi import APIRouter

from services.dashboard_service import (
    DashboardService
)

router = APIRouter()

dashboard_service = DashboardService()


# ==========================================
# Executive Dashboard
# ==========================================

@router.get("/")
def executive_dashboard():

    return (
        dashboard_service
        .executive_dashboard()
    )


# ==========================================
# Executive Summary
# ==========================================

@router.get("/summary")
def executive_summary():

    return (
        dashboard_service
        .executive_summary()
    )


# ==========================================
# Revenue Dashboard
# ==========================================

@router.get("/revenue")
def revenue_dashboard():

    return (
        dashboard_service
        .revenue_dashboard()
    )


# ==========================================
# Claims Dashboard
# ==========================================

@router.get("/claims")
def claims_dashboard():

    return (
        dashboard_service
        .claims_dashboard()
    )


# ==========================================
# Payments Dashboard
# ==========================================

@router.get("/payments")
def payments_dashboard():

    return (
        dashboard_service
        .payments_dashboard()
    )


# ==========================================
# Denials Dashboard
# ==========================================

@router.get("/denials")
def denials_dashboard():

    return (
        dashboard_service
        .denials_dashboard()
    )


# ==========================================
# AR Aging Dashboard
# ==========================================

@router.get("/ar-aging")
def ar_dashboard():

    return (
        dashboard_service
        .ar_dashboard()
    )


# ==========================================
# Patient Billing Dashboard
# ==========================================

@router.get("/patient-billing")
def patient_billing_dashboard():

    return (
        dashboard_service
        .patient_billing_dashboard()
    )


# ==========================================
# Forecast Dashboard
# ==========================================

@router.get("/forecast")
def forecast_dashboard():

    return (
        dashboard_service
        .forecast_dashboard()
    )


# ==========================================
# KPI Dashboard
# ==========================================

@router.get("/kpis")
def dashboard_kpis():

    return (
        dashboard_service
        .dashboard_kpis()
    )