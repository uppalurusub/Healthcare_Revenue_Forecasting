from fastapi import APIRouter

from services.revenue_service import (
    RevenueService
)

router = APIRouter()

revenue_service = RevenueService()

@router.get(
    "/summary"
)
def revenue_summary():

    return (
        revenue_service
        .revenue_summary()
    )

@router.get(
    "/trend"
)
def revenue_trend():

    return (
        revenue_service
        .revenue_trend()
    )

@router.get(
    "/monthly"
)
def monthly_revenue():

    return (
        revenue_service
        .monthly_revenue()
    )


@router.get(
    "/department"
)
def revenue_by_department():

    return (
        revenue_service
        .revenue_by_department()
    )

@router.get(
    "/payer"
)
def revenue_by_payer():

    return (
        revenue_service
        .revenue_by_payer()
    )


@router.get(
    "/collections"
)
def collection_analysis():

    return (
        revenue_service
        .collection_analysis()
    )

@router.get(
    "/leakage"
)
def revenue_leakage():

    return (
        revenue_service
        .revenue_leakage()
    )


@router.get(
    "/leakage"
)
def revenue_leakage():

    return (
        revenue_service
        .revenue_leakage()
    )

@router.get(
    "/top-departments"
)
def top_departments(
        top_n: int = 10
):

    return (
        revenue_service
        .top_departments(top_n)
    )


@router.get(
    "/top-payers"
)
def top_payers(
        top_n: int = 10
):

    return (
        revenue_service
        .top_payers(top_n)
    )


@router.get(
    "/kpis"
)
def revenue_kpis():

    return (
        revenue_service
        .revenue_kpis()
    )

@router.get(
    "/monthly/chart"
)
def monthly_chart():

    return (
        revenue_service
        .monthly_revenue_chart()
    )

@router.get(
    "/department/chart"
)
def department_chart():

    return (
        revenue_service
        .revenue_by_department_chart()
    )

@router.get(
    "/payer/chart"
)
def payer_chart():

    return (
        revenue_service
        .revenue_by_payer_chart()
    )


@router.get(
    "/top-departments/chart"
)
def top_departments(
        top_n: int = 10
):

    return (
        revenue_service
        .top_departments_chart(top_n)
    )


@router.get(
    "/top-payers/chart"
)
def top_payers(
        top_n: int = 10
):

    return (
        revenue_service
        .top_payers_chart(top_n)
    )








@router.get(
    "/distribution/chart"
)
def revenue_distribution_chart():      

    return (
        revenue_service
        .revenue_distribution_chart()
    )

@router.get(
    "/outliers/chart"
)
def revenue_boxplot_chart():      

    return (
        revenue_service
        .revenue_boxplot_chart()
    )

@router.get(
    "/collection-revenue/chart"
)
def revenue_vs_collections_chart():      

    return (
        revenue_service
        .revenue_vs_collections_chart()
    )

@router.get(
    "/correlation/chart"
)
def correlation_heatmap_chart():      

    return (
        revenue_service
        .correlation_heatmap_chart()
    )