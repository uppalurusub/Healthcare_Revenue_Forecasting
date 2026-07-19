import pandas as pd
import numpy as np

from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import (
    ExponentialSmoothing
)

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

class ForecastEvaluation:

    @staticmethod
    def evaluate(
            actual,
            predicted
    ):

        mae = mean_absolute_error(
            actual,
            predicted
        )

        mse = mean_squared_error(
            actual,
            predicted
        )

        rmse = np.sqrt(mse)

        r2 = r2_score(
            actual,
            predicted
        )

        return {

            "mae": round(mae, 2),
            "mse": round(mse, 2),
            "rmse": round(rmse, 2),
            "r2": round(r2, 4)
        }
    
class MovingAverageForecast:

    @staticmethod
    def forecast(
            series,
            window=3,
            periods=6
    ):

        avg = (
            series
            .rolling(window=window)
            .mean()
            .iloc[-1]
        )

        forecast = [avg] * periods

        return forecast
    

class ExponentialForecast:

    @staticmethod
    def forecast(
            series,
            periods=6
    ):

        model = ExponentialSmoothing(
            series,
            trend=None,
            seasonal=None
        )

        fit = model.fit()

        forecast = fit.forecast(
            periods
        )

        return forecast
    

# Holt-Winters Forecast
class HoltWintersForecast:

    @staticmethod
    def forecast(
            series,
            periods=6
    ):

        model = ExponentialSmoothing(
            series,
            trend="add",
            seasonal="add",
            seasonal_periods=12
        )

        fit = model.fit()

        forecast = fit.forecast(
            periods
        )

        return forecast
    
# ARIMA Forecast
class ARIMAForecast:

    @staticmethod
    def forecast(
            series,
            periods=6,
            order=(1, 1, 1)
    ):

        model = ARIMA(
            series,
            order=order
        )

        fit = model.fit()

        forecast = fit.forecast(
            periods
        )

        return forecast
    

#SARIMA Forecast
from statsmodels.tsa.statespace.sarimax import SARIMAX


class SARIMAForecast:

    @staticmethod
    def forecast(
            series,
            periods=6,
            order=(1, 1, 1),
            seasonal_order=(1, 1, 1, 12)
    ):

        model = SARIMAX(
            series,
            order=order,
            seasonal_order=seasonal_order
        )

        fit = model.fit(
            disp=False
        )

        forecast = fit.forecast(
            periods
        )

        return forecast
    

#Revenue Forecast Utility
class RevenueForecasting:

    @staticmethod
    def prepare_monthly_revenue(
            df
    ):

        df["service_date"] = pd.to_datetime(
            df["service_date"]
        )

        monthly = (

            df.groupby(
                pd.Grouper(
                    key="service_date",
                    freq="ME"
                )
            )["gross_revenue"]
            .sum()
            .reset_index()

        )

        return monthly

    @staticmethod
    def prepare_monthly_collection(
            df
    ):

        df["service_date"] = pd.to_datetime(
            df["service_date"]
        )

        monthly = (

            df.groupby(
                pd.Grouper(
                    key="service_date",
                    freq="ME"
                )
            )["payments_collected"]
            .sum()
            .reset_index()

        )

        return monthly
    
#Train-Test Split for Time Series
class TimeSeriesSplit:

    @staticmethod
    def split(
            series,
            test_size=6
    ):

        train = series[:-test_size]

        test = series[-test_size:]

        return train, test
    

#Model Comparison
class ForecastComparison:

    @staticmethod
    def compare_models(
            train,
            test
    ):

        results = []

        # ARIMA

        arima_pred = (
            ARIMAForecast
            .forecast(
                train,
                len(test)
            )
        )

        arima_metrics = (
            ForecastEvaluation
            .evaluate(
                test,
                arima_pred
            )
        )

        results.append({
            "model": "ARIMA",
            **arima_metrics
        })

        # Holt Winters

        hw_pred = (
            HoltWintersForecast
            .forecast(
                train,
                len(test)
            )
        )

        hw_metrics = (
            ForecastEvaluation
            .evaluate(
                test,
                hw_pred
            )
        )

        results.append({
            "model": "Holt-Winters",
            **hw_metrics
        })

        return pd.DataFrame(
            results
        )
    
#Future Revenue Forecast
class FutureRevenueForecast:

    @staticmethod
    def forecast_next_12_months(
            monthly_df
    ):

        revenue_series = (
            monthly_df[
                "gross_revenue"
            ]
        )

        forecast = (
            SARIMAForecast
            .forecast(
                revenue_series,
                periods=12
            )
        )

        future_dates = pd.date_range(
            start=
            monthly_df[
                "service_date"
            ].max(),

            periods=13,

            freq="ME"
        )[1:]

        return pd.DataFrame({

            "forecast_month":
                future_dates,

            "forecast_revenue":
                forecast.values
        })