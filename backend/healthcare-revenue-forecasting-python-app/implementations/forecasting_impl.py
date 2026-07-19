import pandas as pd

from utils.data_loader import DataLoader

from utils.forecasting import (
    RevenueForecasting,
    FutureRevenueForecast,
    ForecastComparison,
    ForecastEvaluation,
    TimeSeriesSplit,
    SARIMAForecast
)


class ForecastingImplementation:

    def __init__(self):

        self.revenue_df = (
            DataLoader.load_revenue()
        )

        self.payments_df = (
            DataLoader.load_payments()
        )

        self.ar_df = (
            DataLoader.load_ar_aging()
        )

        self.revenue_df["service_date"] = pd.to_datetime(
            self.revenue_df["service_date"],
            errors="coerce"
        )

        
        self.ar_df["as_of_date"] = pd.to_datetime(
            self.ar_df["as_of_date"],
            errors="coerce"
        )

    #Forecast KPIs
    def forecast_kpis(self):

        summary = (
            self.forecast_summary()
        )

        evaluation = (
            self.forecast_evaluation()
        )

        comparison = (
            self.model_comparison()
        )

        best_model = min(
            comparison,
            key=lambda x: x["rmse"]
        )["model"]

        return {

            "forecast_periods": 12,

            "projected_revenue":
                summary[
                    "projected_revenue"
                ],

            "projected_collections":
                summary[
                    "projected_collections"
                ],

            "projected_ar":
                summary[
                    "projected_ar"
                ],

            "best_model":
                best_model,

            "forecast_accuracy":
                round(
                    (
                        1 -
                        (
                            evaluation["mae"]
                            /
                            summary[
                                "projected_revenue"
                            ]
                        )
                    ) * 100,
                    2
                )
        }
    
    #Forecast Summary
    def forecast_summary(self):

        revenue = pd.DataFrame(
            self.revenue_forecast(12)
        )

        collections = pd.DataFrame(
            self.collection_forecast(12)
        )

        ar = pd.DataFrame(
            self.ar_forecast(12)
        )

        return {

            "projected_revenue":
                float(
                    revenue[
                        "forecast_revenue"
                    ].sum()
                ),

            "projected_collections":
                float(
                    collections[
                        "forecast_collections"
                    ].sum()
                ),

            "projected_ar":
                float(
                    ar[
                        "forecast_ar_balance"
                    ].sum()
                )
        }
    

    #Forecast Evaluation
    def forecast_evaluation(self):

        monthly = (
            RevenueForecasting
            .prepare_monthly_revenue(
                self.revenue_df
            )
        )

        series = (
            monthly[
                "gross_revenue"
            ]
        )

        train, test = (
            TimeSeriesSplit
            .split(series)
        )

        predictions = (
            SARIMAForecast
            .forecast(
                train,
                len(test)
            )
        )

        metrics = (
            ForecastEvaluation
            .evaluate(
                test,
                predictions
            )
        )

        return metrics
    
    #Model Comparison
    def model_comparison(self):

        monthly = (
            RevenueForecasting
            .prepare_monthly_revenue(
                self.revenue_df
            )
        )

        series = (
            monthly[
                "gross_revenue"
            ]
        )

        train, test = (
            TimeSeriesSplit
            .split(series)
        )

        results = (
            ForecastComparison
            .compare_models(
                train,
                test
            )
        )

        return results.to_dict(
            orient="records"
        )
    
    #Scenario Forecast
    def scenario_forecast(
            self,
            periods=12
    ):

        forecast = pd.DataFrame(
            self.revenue_forecast(
                periods
            )
        )

        forecast[
            "base_forecast"
        ] = (
            forecast[
                "forecast_revenue"
            ]
        )

        forecast[
            "optimistic_forecast"
        ] = (
            forecast[
                "forecast_revenue"
            ] * 1.10
        )

        forecast[
            "pessimistic_forecast"
        ] = (
            forecast[
                "forecast_revenue"
            ] * 0.90
        )

        return forecast.to_dict(
            orient="records"
        )
    
    #Revenue Growth Forecast
    def revenue_growth_forecast(
            self,
            periods=12
    ):

        forecast = pd.DataFrame(
            self.revenue_forecast(
                periods
            )
        )

        forecast[
            "growth_pct"
        ] = (

            forecast[
                "forecast_revenue"
            ]
            .pct_change()
            * 100

        )

        return forecast.fillna(
            0
        ).to_dict(
            orient="records"
        )
    
    #AR Forecast
    def ar_forecast(
            self,
            periods=12
    ):

        monthly = (

            self.ar_df.groupby(
                pd.Grouper(
                    key="as_of_date",
                    freq="ME"
                )
            )["outstanding_balance"]
            .sum()
            .reset_index()

        )

        series = (
            monthly[
                "outstanding_balance"
            ]
        )

        forecast = (
            SARIMAForecast
            .forecast(
                series,
                periods
            )
        )

        future_dates = pd.date_range(

            start=
            monthly[
                "as_of_date"
            ].max(),

            periods=periods + 1,

            freq="ME"

        )[1:]

        result = pd.DataFrame({

            "forecast_month":
                future_dates,

            "forecast_ar_balance":
                forecast.values

        })

        return result.to_dict(
            orient="records"
        )
    

    #Collection Forecast
    def collection_forecast(
            self,
            periods=12
    ):

        monthly = (
            RevenueForecasting
            .prepare_monthly_collection(
                self.revenue_df
            )
        )

        series = (
            monthly[
                "payments_collected"
            ]
        )

        forecast = (
            SARIMAForecast
            .forecast(
                series,
                periods
            )
        )

        future_dates = pd.date_range(

            start=
            monthly[
                "service_date"
            ].max(),

            periods=periods + 1,

            freq="ME"

        )[1:]

        result = pd.DataFrame({

            "forecast_month":
                future_dates,

            "forecast_collections":
                forecast.values

        })

        return result.to_dict(
            orient="records"
        )
    

    #Revenue Forecast
    def revenue_forecast(
            self,
            periods=12
    ):

        monthly = (
            RevenueForecasting
            .prepare_monthly_revenue(
                self.revenue_df
            )
        )

        forecast_df = (
            FutureRevenueForecast
            .forecast_next_12_months(
                monthly
            )
        )

        return (
            forecast_df
            .head(periods)
            .to_dict(
                orient="records"
            )
        )