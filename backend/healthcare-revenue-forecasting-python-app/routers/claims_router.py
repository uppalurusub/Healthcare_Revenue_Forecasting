from fastapi import APIRouter

from services.claims_service import (
    ClaimsService
)

router = APIRouter()

claims_service = ClaimsService()


@router.get("/summary")
def claims_summary():
    return claims_service.claims_summary()


@router.get("/trend")
def claims_trend():
    return claims_service.claims_trend()


@router.get("/monthly")
def monthly_claims():
    return claims_service.monthly_claims()


@router.get("/status")
def claim_status():
    return claims_service.claim_status_analysis()


@router.get("/denials")
def denial_analysis():
    return claims_service.denial_analysis()


@router.get("/denial-reasons")
def denial_reasons():
    return claims_service.denial_reasons()


@router.get("/payer")
def payer_analysis():
    return claims_service.payer_analysis()


@router.get("/department")
def department_analysis():
    return claims_service.department_analysis()


@router.get("/reimbursement")
def reimbursement_analysis():
    return claims_service.reimbursement_analysis()


@router.get("/top-denial-reasons")
def top_denial_reasons(
        top_n: int = 10
):
    return claims_service.top_denial_reasons(top_n)


@router.get("/kpis")
def claims_kpis():
    return claims_service.claims_kpis()