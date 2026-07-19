from implementations.forecasting_impl import (
    ForecastingImplementation
)


class ForecastingService:

    def __init__(self):

        self.forecasting_impl = (
            ForecastingImplementation()
        )

    # ==========================================
    # Revenue Forecast
    # ==========================================

    def revenue_forecast(
            self,
            periods=12
    ):

        return (
            self.forecasting_impl
            .revenue_forecast(periods)
        )

    # ==========================================
    # Collection Forecast
    # ==========================================

    def collection_forecast(
            self,
            periods=12
    ):

        return (
            self.forecasting_impl
            .collection_forecast(periods)
        )

    # ==========================================
    # AR Forecast
    # ==========================================

    def ar_forecast(
            self,
            periods=12
    ):

        return (
            self.forecasting_impl
            .ar_forecast(periods)
        )

    # ==========================================
    # Revenue Growth Forecast
    # ==========================================

    def revenue_growth_forecast(
            self,
            periods=12
    ):

        return (
            self.forecasting_impl
            .revenue_growth_forecast(
                periods
            )
        )

    # ==========================================
    # Scenario Forecast
    # ==========================================

    def scenario_forecast(
            self,
            periods=12
    ):

        return (
            self.forecasting_impl
            .scenario_forecast(
                periods
            )
        )

    # ==========================================
    # Model Comparison
    # ==========================================

    def model_comparison(self):

        return (
            self.forecasting_impl
            .model_comparison()
        )

    # ==========================================
    # Forecast Evaluation
    # ==========================================

    def forecast_evaluation(self):

        return (
            self.forecasting_impl
            .forecast_evaluation()
        )

    # ==========================================
    # Forecast Summary
    # ==========================================

    def forecast_summary(self):

        return (
            self.forecasting_impl
            .forecast_summary()
        )

    # ==========================================
    # Forecast KPIs
    # ==========================================

    def forecast_kpis(self):

        return (
            self.forecasting_impl
            .forecast_kpis()
        )