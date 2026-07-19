import pandas as pd

from utils.data_loader import DataLoader


class DenialsImplementation:

    def __init__(self):

        self.df = DataLoader.load_denials()

        self.df["denial_date"] = pd.to_datetime(
            self.df["denial_date"]
        )

    # ==========================================
    # Denial Summary
    # ==========================================

    def denial_summary(self):

        total_denials = len(self.df)

        total_denied_amount = (
            self.df["claim_amount"]
            .sum()
        )

        recovered_amount = (
            self.df["recovered_amount"]
            .sum()
        )

        unresolved_amount = (
            total_denied_amount
            - recovered_amount
        )

        return {

            "total_denials":
                total_denials,

            "total_denied_amount":
                float(
                    total_denied_amount
                ),

            "recovered_amount":
                float(
                    recovered_amount
                ),

            "unresolved_amount":
                float(
                    unresolved_amount
                )
        }

    # ==========================================
    # Denial Trend
    # ==========================================

    def denial_trend(self):

        trend = (

            self.df.groupby(
                "denial_date"
            )
            .size()
            .reset_index(
                name="denial_count"
            )

        )

        return trend.to_dict(
            orient="records"
        )

    # ==========================================
    # Monthly Denials
    # ==========================================

    def monthly_denials(self):

        monthly = (

            self.df.groupby(
                pd.Grouper(
                    key="denial_date",
                    freq="ME"
                )
            )
            .size()
            .reset_index(
                name="denial_count"
            )

        )

        return monthly.to_dict(
            orient="records"
        )

    # ==========================================
    # Denial Reasons
    # ==========================================

    def denial_reasons(self):

        reasons = (

            self.df[
                "denial_reason"
            ]
            .value_counts()
            .reset_index()

        )

        reasons.columns = [
            "denial_reason",
            "count"
        ]

        return reasons.to_dict(
            orient="records"
        )

    # ==========================================
    # Denial Categories
    # ==========================================

    def denial_categories(self):

        categories = (

            self.df[
                "denial_category"
            ]
            .value_counts()
            .reset_index()

        )

        categories.columns = [
            "denial_category",
            "count"
        ]

        return categories.to_dict(
            orient="records"
        )

    # ==========================================
    # Department Analysis
    # ==========================================

    def department_analysis(self):

        department = (

            self.df.groupby(
                "department"
            )["claim_amount"]
            .sum()
            .reset_index()

        )

        return department.to_dict(
            orient="records"
        )

    # ==========================================
    # Payer Analysis
    # ==========================================

    def payer_analysis(self):

        payer = (

            self.df.groupby(
                "payer_type"
            )["claim_amount"]
            .sum()
            .reset_index()

        )

        return payer.to_dict(
            orient="records"
        )

    # ==========================================
    # Appeal Analysis
    # ==========================================

    def appeal_analysis(self):

        appeal = (

            self.df[
                "appeal_status"
            ]
            .value_counts()
            .reset_index()

        )

        appeal.columns = [
            "appeal_status",
            "count"
        ]

        return appeal.to_dict(
            orient="records"
        )

    # ==========================================
    # Recovery Analysis
    # ==========================================

    def recovery_analysis(self):

        total_denied = (
            self.df["claim_amount"]
            .sum()
        )

        total_recovered = (
            self.df["recovered_amount"]
            .sum()
        )

        recovery_rate = round(

            (
                total_recovered
                /
                total_denied
            ) * 100,

            2

        )

        return {

            "total_denied_amount":
                float(
                    total_denied
                ),

            "total_recovered_amount":
                float(
                    total_recovered
                ),

            "recovery_rate":
                recovery_rate
        }

    # ==========================================
    # Resolution Analysis
    # ==========================================

    def resolution_analysis(self):

        return {

            "average_days":
                round(
                    self.df[
                        "days_to_resolution"
                    ].mean(),
                    2
                ),

            "minimum_days":
                int(
                    self.df[
                        "days_to_resolution"
                    ].min()
                ),

            "maximum_days":
                int(
                    self.df[
                        "days_to_resolution"
                    ].max()
                )
        }

    # ==========================================
    # Top Denial Reasons
    # ==========================================

    def top_denial_reasons(
            self,
            top_n=10
    ):

        reasons = (

            self.df[
                "denial_reason"
            ]
            .value_counts()
            .head(top_n)
            .reset_index()

        )

        reasons.columns = [
            "denial_reason",
            "count"
        ]

        return reasons.to_dict(
            orient="records"
        )

    # ==========================================
    # Revenue Leakage Analysis
    # ==========================================

    def revenue_leakage(self):

        total_denied = (
            self.df["claim_amount"]
            .sum()
        )

        recovered = (
            self.df["recovered_amount"]
            .sum()
        )

        leakage = (
            total_denied
            - recovered
        )

        return {

            "total_denied_amount":
                float(
                    total_denied
                ),

            "recovered_amount":
                float(
                    recovered
                ),

            "revenue_leakage":
                float(
                    leakage
                )
        }

    # ==========================================
    # Denial KPIs
    # ==========================================

    def denial_kpis(self):

        total_denials = len(self.df)

        total_denied_amount = (
            self.df["claim_amount"]
            .sum()
        )

        recovered_amount = (
            self.df["recovered_amount"]
            .sum()
        )

        recovery_rate = round(

            (
                recovered_amount
                /
                total_denied_amount
            ) * 100,

            2

        )

        appeal_rate = round(

            (
                len(
                    self.df[
                        self.df[
                            "appeal_status"
                        ].isin(
                            [
                                "Appealed",
                                "Overturned"
                            ]
                        )
                    ]
                )
                /
                total_denials
            ) * 100,

            2

        )

        return {

            "total_denials":
                total_denials,

            "total_denied_amount":
                float(
                    total_denied_amount
                ),

            "recovered_amount":
                float(
                    recovered_amount
                ),

            "recovery_rate":
                recovery_rate,

            "appeal_rate":
                appeal_rate,

            "average_resolution_days":
                round(
                    self.df[
                        "days_to_resolution"
                    ].mean(),
                    2
                )
        }