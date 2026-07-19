import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

class ForecastVisualization:

    # ==========================================
    # Actual vs Forecast
    # ==========================================

    @staticmethod
    def actual_vs_forecast(
            actual_df,
            forecast_df,
            date_col="service_date",
            actual_col="gross_revenue",
            forecast_col="forecast_revenue"
    ):

        plt.figure(figsize=(14, 6))

        plt.plot(
            actual_df[date_col],
            actual_df[actual_col],
            label="Actual Revenue"
        )

        plt.plot(
            forecast_df["forecast_month"],
            forecast_df[forecast_col],
            label="Forecast Revenue"
        )

        plt.title(
            "Actual Revenue vs Forecast Revenue"
        )

        plt.xlabel("Date")
        plt.ylabel("Revenue")

        plt.legend()

        plt.tight_layout()

        return plt

    # ==========================================
    # Forecast Trend
    # ==========================================

    @staticmethod
    def forecast_trend(
            forecast_df
    ):

        plt.figure(figsize=(12, 6))

        sns.lineplot(
            data=forecast_df,
            x="forecast_month",
            y="forecast_revenue"
        )

        plt.title(
            "Revenue Forecast Trend"
        )

        plt.xlabel("Month")
        plt.ylabel("Forecast Revenue")

        plt.tight_layout()

        return plt

    # ==========================================
    # Forecast Bar Chart
    # ==========================================

    @staticmethod
    def forecast_bar(
            forecast_df
    ):

        plt.figure(figsize=(12, 6))

        sns.barplot(
            data=forecast_df,
            x="forecast_month",
            y="forecast_revenue"
        )

        plt.xticks(rotation=45)

        plt.title(
            "Forecast Revenue by Month"
        )

        plt.tight_layout()

        return plt
    

#Confidence Interval Visualization
class ConfidenceIntervalVisualization:

    @staticmethod
    def confidence_interval_plot(
            forecast_df
    ):

        plt.figure(figsize=(14, 6))

        plt.plot(
            forecast_df["forecast_month"],
            forecast_df["forecast_revenue"],
            label="Forecast"
        )

        plt.fill_between(
            forecast_df["forecast_month"],
            forecast_df["lower_ci"],
            forecast_df["upper_ci"],
            alpha=0.3,
            label="95% Confidence Interval"
        )

        plt.title(
            "Revenue Forecast Confidence Interval"
        )

        plt.legend()

        plt.tight_layout()

        return plt
    
#Forecast Error Analysis
class ForecastErrorVisualization:

    @staticmethod
    def residual_plot(
            actual,
            predicted
    ):

        residuals = actual - predicted

        plt.figure(figsize=(10, 6))

        sns.histplot(
            residuals,
            kde=True
        )

        plt.title(
            "Forecast Residual Distribution"
        )

        plt.xlabel("Residual Error")

        plt.tight_layout()

        return plt

    @staticmethod
    def actual_vs_predicted(
            actual,
            predicted
    ):

        plt.figure(figsize=(8, 6))

        sns.scatterplot(
            x=actual,
            y=predicted
        )

        plt.title(
            "Actual vs Predicted Revenue"
        )

        plt.xlabel("Actual")
        plt.ylabel("Predicted")

        plt.tight_layout()

        return plt
    
#Model Comparison Visualization
class ModelComparisonVisualization:

    @staticmethod
    def compare_rmse(
            results_df
    ):

        plt.figure(figsize=(10, 6))

        sns.barplot(
            data=results_df,
            x="model",
            y="rmse"
        )

        plt.title(
            "Model Comparison (RMSE)"
        )

        plt.tight_layout()

        return plt

    @staticmethod
    def compare_mae(
            results_df
    ):

        plt.figure(figsize=(10, 6))

        sns.barplot(
            data=results_df,
            x="model",
            y="mae"
        )

        plt.title(
            "Model Comparison (MAE)"
        )

        plt.tight_layout()

        return plt
    
#Revenue Growth Forecast
class RevenueGrowthVisualization:

    @staticmethod
    def revenue_growth_forecast(
            forecast_df
    ):

        forecast_df = forecast_df.copy()

        forecast_df["growth_pct"] = (

            forecast_df["forecast_revenue"]
            .pct_change()
            * 100

        )

        plt.figure(figsize=(12, 6))

        sns.lineplot(
            data=forecast_df,
            x="forecast_month",
            y="growth_pct"
        )

        plt.title(
            "Forecast Revenue Growth %"
        )

        plt.ylabel(
            "Growth Percentage"
        )

        plt.tight_layout()

        return plt
    
#Scenario Forecast Visualization
class ScenarioForecastVisualization:

    @staticmethod
    def scenario_forecast(
            forecast_df
    ):

        plt.figure(figsize=(14, 6))

        plt.plot(
            forecast_df["forecast_month"],
            forecast_df["base_forecast"],
            label="Base"
        )

        plt.plot(
            forecast_df["forecast_month"],
            forecast_df["optimistic_forecast"],
            label="Optimistic"
        )

        plt.plot(
            forecast_df["forecast_month"],
            forecast_df["pessimistic_forecast"],
            label="Pessimistic"
        )

        plt.title(
            "Scenario Revenue Forecast"
        )

        plt.legend()

        plt.tight_layout()

        return plt
    
#Collections Forecast Visualization
class CollectionForecastVisualization:

    @staticmethod
    def collections_forecast(
            forecast_df
    ):

        plt.figure(figsize=(12, 6))

        sns.lineplot(
            data=forecast_df,
            x="forecast_month",
            y="forecast_collections"
        )

        plt.title(
            "Collection Forecast"
        )

        plt.tight_layout()

        return plt
    
#AR Forecast Visualization
class ARForecastVisualization:

    @staticmethod
    def ar_forecast(
            forecast_df
    ):

        plt.figure(figsize=(12, 6))

        sns.lineplot(
            data=forecast_df,
            x="forecast_month",
            y="forecast_ar_balance"
        )

        plt.title(
            "Accounts Receivable Forecast"
        )

        plt.tight_layout()

        return plt