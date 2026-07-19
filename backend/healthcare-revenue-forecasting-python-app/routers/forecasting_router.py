from fastapi import APIRouter

from services.forecasting_service import (
    ForecastingService
)

router = APIRouter()

forecast_service = (
    ForecastingService()
)


# ==========================================
# Revenue Forecast
# ==========================================

@router.get("/revenue")
def revenue_forecast(
        periods: int = 12
):

    return (
        forecast_service
        .revenue_forecast(periods)
    )


# ==========================================
# Collection Forecast
# ==========================================

@router.get("/collections")
def collection_forecast(
        periods: int = 12
):

    return (
        forecast_service
        .collection_forecast(periods)
    )


# ==========================================
# AR Forecast
# ==========================================

@router.get("/ar")
def ar_forecast(
        periods: int = 12
):

    return (
        forecast_service
        .ar_forecast(periods)
    )


# ==========================================
# Revenue Growth Forecast
# ==========================================

@router.get("/growth")
def revenue_growth_forecast(
        periods: int = 12
):

    return (
        forecast_service
        .revenue_growth_forecast(
            periods
        )
    )


# ==========================================
# Scenario Forecast
# ==========================================

@router.get("/scenario")
def scenario_forecast(
        periods: int = 12
):

    return (
        forecast_service
        .scenario_forecast(periods)
    )


# ==========================================
# Model Comparison
# ==========================================

@router.get("/model-comparison")
def model_comparison():

    return (
        forecast_service
        .model_comparison()
    )


# ==========================================
# Forecast Evaluation
# ==========================================

@router.get("/evaluation")
def forecast_evaluation():

    return (
        forecast_service
        .forecast_evaluation()
    )


# ==========================================
# Forecast Summary
# ==========================================

@router.get("/summary")
def forecast_summary():

    return (
        forecast_service
        .forecast_summary()
    )


# ==========================================
# Forecast KPIs
# ==========================================

@router.get("/kpis")
def forecast_kpis():

    return (
        forecast_service
        .forecast_kpis()
    )