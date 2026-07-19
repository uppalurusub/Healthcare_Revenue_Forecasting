import pandas as pd

from utils.data_loader import DataLoader


class ARAgingImplementation:

    def __init__(self):

        self.df = DataLoader.load_ar_aging()

        self.df["as_of_date"] = pd.to_datetime(
            self.df["as_of_date"]
        )

    # ==========================================
    # AR Summary
    # ==========================================

    def ar_summary(self):

        total_ar_balance = (
            self.df["outstanding_balance"]
            .sum()
        )

        expected_collection = (
            self.df["expected_collection"]
            .sum()
        )

        average_days = (
            self.df["days_in_ar"]
            .mean()
        )

        high_risk_balance = (

            self.df[
                self.df["risk_level"]
                == "High"
            ]["outstanding_balance"]
            .sum()

        )

        return {

            "total_ar_balance":
                float(total_ar_balance),

            "expected_collection":
                float(expected_collection),

            "average_days_in_ar":
                round(average_days, 2),

            "high_risk_balance":
                float(high_risk_balance)
        }

    # ==========================================
    # AR Trend
    # ==========================================

    def ar_trend(self):

        trend = (

            self.df.groupby(
                "as_of_date"
            )["outstanding_balance"]
            .sum()
            .reset_index()

        )

        return trend.to_dict(
            orient="records"
        )

    # ==========================================
    # Monthly AR
    # ==========================================

    def monthly_ar(self):

        monthly = (

            self.df.groupby(
                pd.Grouper(
                    key="as_of_date",
                    freq="ME"
                )
            )["outstanding_balance"]
            .sum()
            .reset_index()

        )

        return monthly.to_dict(
            orient="records"
        )

    # ==========================================
    # Aging Bucket Analysis
    # ==========================================

    def aging_bucket_analysis(self):

        buckets = (

            self.df.groupby(
                "aging_bucket"
            )["outstanding_balance"]
            .sum()
            .reset_index()

        )

        return buckets.to_dict(
            orient="records"
        )

    # ==========================================
    # Collection Status Analysis
    # ==========================================

    def collection_status_analysis(self):

        status = (

            self.df.groupby(
                "collection_status"
            )["outstanding_balance"]
            .sum()
            .reset_index()

        )

        return status.to_dict(
            orient="records"
        )

    # ==========================================
    # Risk Analysis
    # ==========================================

    def risk_analysis(self):

        risk = (

            self.df.groupby(
                "risk_level"
            )["outstanding_balance"]
            .agg([
                "count",
                "sum"
            ])
            .reset_index()

        )

        return risk.to_dict(
            orient="records"
        )

    # ==========================================
    # Payer Analysis
    # ==========================================

    def payer_analysis(self):

        payer = (

            self.df.groupby(
                "payer_type"
            )["outstanding_balance"]
            .sum()
            .reset_index()

        )

        return payer.to_dict(
            orient="records"
        )

    # ==========================================
    # Department Analysis
    # ==========================================

    def department_analysis(self):

        department = (

            self.df.groupby(
                "department"
            )["outstanding_balance"]
            .sum()
            .reset_index()

        )

        return department.to_dict(
            orient="records"
        )

    # ==========================================
    # Expected Collections
    # ==========================================

    def expected_collections(self):

        collections = (

            self.df.groupby(
                "aging_bucket"
            )["expected_collection"]
            .sum()
            .reset_index()

        )

        return collections.to_dict(
            orient="records"
        )

    # ==========================================
    # High Risk Accounts
    # ==========================================

    def high_risk_accounts(self):

        high_risk = (

            self.df[
                self.df["risk_level"]
                .isin(
                    ["High", "Critical"]
                )
            ]
            .sort_values(
                by="outstanding_balance",
                ascending=False
            )
            .head(50)
        )

        return high_risk.to_dict(
            orient="records"
        )

    # ==========================================
    # Top Payers
    # ==========================================

    def top_payers(
            self,
            top_n=10
    ):

        payers = (

            self.df.groupby(
                "payer_type"
            )["outstanding_balance"]
            .sum()
            .sort_values(
                ascending=False
            )
            .head(top_n)
            .reset_index()

        )

        return payers.to_dict(
            orient="records"
        )

    # ==========================================
    # AR KPIs
    # ==========================================

    def ar_kpis(self):

        total_balance = (
            self.df[
                "outstanding_balance"
            ].sum()
        )

        expected_collection = (
            self.df[
                "expected_collection"
            ].sum()
        )

        collection_potential = round(

            (
                expected_collection
                /
                total_balance
            ) * 100,

            2

        ) if total_balance > 0 else 0

        avg_days = round(

            self.df[
                "days_in_ar"
            ].mean(),

            2

        )

        high_risk_accounts = len(

            self.df[
                self.df[
                    "risk_level"
                ] == "High"
            ]

        )

        critical_accounts = len(

            self.df[
                self.df[
                    "risk_level"
                ] == "Critical"
            ]

        )

        return {

            "total_ar_balance":
                float(total_balance),

            "expected_collection":
                float(
                    expected_collection
                ),

            "collection_potential":
                collection_potential,

            "average_days_in_ar":
                avg_days,

            "high_risk_accounts":
                high_risk_accounts,

            "critical_accounts":
                critical_accounts
        }