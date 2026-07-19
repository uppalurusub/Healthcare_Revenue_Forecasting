from fastapi import APIRouter

from services.patient_billing_service import (
    PatientBillingService
)

router = APIRouter()

billing_service = (
    PatientBillingService()
)


# ==========================================
# Billing Summary
# ==========================================

@router.get("/summary")
def billing_summary():

    return (
        billing_service
        .billing_summary()
    )


# ==========================================
# Billing Trend
# ==========================================

@router.get("/trend")
def billing_trend():

    return (
        billing_service
        .billing_trend()
    )


# ==========================================
# Monthly Billing
# ==========================================

@router.get("/monthly")
def monthly_billing():

    return (
        billing_service
        .monthly_billing()
    )


# ==========================================
# Billing Status Analysis
# ==========================================

@router.get("/status")
def billing_status():

    return (
        billing_service
        .billing_status_analysis()
    )


# ==========================================
# Payment Plan Analysis
# ==========================================

@router.get("/payment-plans")
def payment_plan_analysis():

    return (
        billing_service
        .payment_plan_analysis()
    )


# ==========================================
# Department Analysis
# ==========================================

@router.get("/department")
def department_analysis():

    return (
        billing_service
        .department_analysis()
    )


# ==========================================
# Payer Analysis
# ==========================================

@router.get("/payer")
def payer_analysis():

    return (
        billing_service
        .payer_analysis()
    )


# ==========================================
# Outstanding Balances
# ==========================================

@router.get("/outstanding-balances")
def outstanding_balances():

    return (
        billing_service
        .outstanding_balances()
    )


# ==========================================
# Collection Analysis
# ==========================================

@router.get("/collections")
def collection_analysis():

    return (
        billing_service
        .collection_analysis()
    )


# ==========================================
# Payment Plan Performance
# ==========================================

@router.get("/payment-plan-performance")
def payment_plan_performance():

    return (
        billing_service
        .payment_plan_performance()
    )


# ==========================================
# Top Outstanding Patients
# ==========================================

@router.get("/top-patients")
def top_outstanding_patients(
        top_n: int = 20
):

    return (
        billing_service
        .top_outstanding_patients(
            top_n
        )
    )


# ==========================================
# Billing KPIs
# ==========================================

@router.get("/kpis")
def billing_kpis():

    return (
        billing_service
        .billing_kpis()
    )