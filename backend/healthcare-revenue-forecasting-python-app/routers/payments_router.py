from fastapi import APIRouter

from services.payments_service import (
    PaymentsService
)

router = APIRouter()

payments_service = PaymentsService()


# ==========================================
# Payment Summary
# ==========================================

@router.get("/summary")
def payment_summary():

    return (
        payments_service
        .payment_summary()
    )


# ==========================================
# Payment Trend
# ==========================================

@router.get("/trend")
def payment_trend():

    return (
        payments_service
        .payment_trend()
    )


# ==========================================
# Monthly Payments
# ==========================================

@router.get("/monthly")
def monthly_payments():

    return (
        payments_service
        .monthly_payments()
    )


# ==========================================
# Payment Status Analysis
# ==========================================

@router.get("/status")
def payment_status():

    return (
        payments_service
        .payment_status_analysis()
    )


# ==========================================
# Insurance Payments
# ==========================================

@router.get("/insurance")
def insurance_payments():

    return (
        payments_service
        .insurance_payments()
    )


# ==========================================
# Patient Payments
# ==========================================

@router.get("/patient")
def patient_payments():

    return (
        payments_service
        .patient_payments()
    )


# ==========================================
# Payer Analysis
# ==========================================

@router.get("/payer")
def payer_analysis():

    return (
        payments_service
        .payer_analysis()
    )


# ==========================================
# Payment Method Analysis
# ==========================================

@router.get("/payment-method")
def payment_method_analysis():

    return (
        payments_service
        .payment_method_analysis()
    )


# ==========================================
# Collection Analysis
# ==========================================

@router.get("/collections")
def collection_analysis():

    return (
        payments_service
        .collection_analysis()
    )


# ==========================================
# Average Payment Days
# ==========================================

@router.get("/days-to-payment")
def days_to_payment():

    return (
        payments_service
        .days_to_payment_analysis()
    )


# ==========================================
# Top Payers
# ==========================================

@router.get("/top-payers")
def top_payers(
        top_n: int = 10
):

    return (
        payments_service
        .top_payers(top_n)
    )


# ==========================================
# Payment KPIs
# ==========================================

@router.get("/kpis")
def payment_kpis():

    return (
        payments_service
        .payment_kpis()
    )