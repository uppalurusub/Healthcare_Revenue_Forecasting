from fastapi import APIRouter

from services.denials_service import (
    DenialsService
)

router = APIRouter()

denials_service = DenialsService()


# ==========================================
# Denial Summary
# ==========================================

@router.get("/summary")
def denial_summary():

    return (
        denials_service
        .denial_summary()
    )


# ==========================================
# Denial Trend
# ==========================================

@router.get("/trend")
def denial_trend():

    return (
        denials_service
        .denial_trend()
    )


# ==========================================
# Monthly Denials
# ==========================================

@router.get("/monthly")
def monthly_denials():

    return (
        denials_service
        .monthly_denials()
    )


# ==========================================
# Denial Reasons
# ==========================================

@router.get("/reasons")
def denial_reasons():

    return (
        denials_service
        .denial_reasons()
    )


# ==========================================
# Denial Categories
# ==========================================

@router.get("/categories")
def denial_categories():

    return (
        denials_service
        .denial_categories()
    )


# ==========================================
# Department Analysis
# ==========================================

@router.get("/department")
def department_analysis():

    return (
        denials_service
        .department_analysis()
    )


# ==========================================
# Payer Analysis
# ==========================================

@router.get("/payer")
def payer_analysis():

    return (
        denials_service
        .payer_analysis()
    )


# ==========================================
# Appeal Analysis
# ==========================================

@router.get("/appeals")
def appeal_analysis():

    return (
        denials_service
        .appeal_analysis()
    )


# ==========================================
# Recovery Analysis
# ==========================================

@router.get("/recovery")
def recovery_analysis():

    return (
        denials_service
        .recovery_analysis()
    )


# ==========================================
# Resolution Analysis
# ==========================================

@router.get("/resolution")
def resolution_analysis():

    return (
        denials_service
        .resolution_analysis()
    )


# ==========================================
# Top Denial Reasons
# ==========================================

@router.get("/top-reasons")
def top_denial_reasons(
        top_n: int = 10
):

    return (
        denials_service
        .top_denial_reasons(top_n)
    )


# ==========================================
# Revenue Leakage
# ==========================================

@router.get("/revenue-leakage")
def revenue_leakage():

    return (
        denials_service
        .revenue_leakage()
    )


# ==========================================
# Denial KPIs
# ==========================================

@router.get("/kpis")
def denial_kpis():

    return (
        denials_service
        .denial_kpis()
    )