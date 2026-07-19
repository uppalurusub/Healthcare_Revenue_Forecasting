from prophet import Prophet


class ProphetForecast:

    @staticmethod
    def forecast(
            monthly_df,
            periods=12
    ):

        prophet_df = monthly_df.rename(
            columns={
                "service_date": "ds",
                "gross_revenue": "y"
            }
        )

        model = Prophet()

        model.fit(
            prophet_df
        )

        future = model.make_future_dataframe(
            periods=periods,
            freq="M"
        )

        forecast = model.predict(
            future
        )

        return forecast