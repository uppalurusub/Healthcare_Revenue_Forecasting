import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


class RevenueMetrics:

    @staticmethod
    def total_revenue(df):

        return float(
            df["gross_revenue"].sum()
        )

    @staticmethod
    def average_revenue(df):

        return float(
            df["gross_revenue"].mean()
        )

    @staticmethod
    def revenue_growth(df):

        revenue = (
            df.groupby("year")
            ["gross_revenue"]
            .sum()
        )

        if len(revenue) < 2:
            return 0

        return round(
            (
                (revenue.iloc[-1] -
                 revenue.iloc[-2])
                /
                revenue.iloc[-2]
            ) * 100,
            2
        )

    @staticmethod
    def collection_rate(df):

        return round(
            (
                df["payments_collected"].sum()
                /
                df["gross_revenue"].sum()
            ) * 100,
            2
        )

    @staticmethod
    def reimbursement_rate(df):

        return round(
            (
                df["payments_collected"].sum()
                /
                df["expected_reimbursement"].sum()
            ) * 100,
            2
        )

    @staticmethod
    def revenue_leakage(df):

        return float(
            (
                df["expected_reimbursement"]
                -
                df["payments_collected"]
            ).sum()
        )