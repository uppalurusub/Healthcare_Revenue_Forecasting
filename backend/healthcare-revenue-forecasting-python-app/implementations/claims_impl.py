import pandas as pd

from utils.data_loader import DataLoader


class ClaimsImplementation:

    def __init__(self):

        self.df = DataLoader.load_claims()

        self.df["service_date"] = pd.to_datetime(
            self.df["service_date"]
        )

    # ==========================================
    # Claims Summary
    # ==========================================

    def claims_summary(self):

        total_claims = len(self.df)

        approved = len(
            self.df[
                self.df["claim_status"]
                == "Approved"
            ]
        )

        denied = len(
            self.df[
                self.df["claim_status"]
                == "Denied"
            ]
        )

        pending = len(
            self.df[
                self.df["claim_status"]
                == "Pending"
            ]
        )

        paid = len(
            self.df[
                self.df["claim_status"]
                == "Paid"
            ]
        )

        return {

            "total_claims": total_claims,

            "approved_claims": approved,

            "denied_claims": denied,

            "pending_claims": pending,

            "paid_claims": paid,

            "approval_rate":
                round(
                    (approved / total_claims)
                    * 100,
                    2
                ),

            "denial_rate":
                round(
                    (denied / total_claims)
                    * 100,
                    2
                )
        }

    # ==========================================
    # Claims Trend
    # ==========================================

    def claims_trend(self):

        trend = (

            self.df
            .groupby("service_date")
            .size()
            .reset_index(
                name="claim_count"
            )

        )

        return trend.to_dict(
            orient="records"
        )

    # ==========================================
    # Monthly Claims
    # ==========================================

    def monthly_claims(self):

        monthly = (

            self.df.groupby(
                pd.Grouper(
                    key="service_date",
                    freq="ME"
                )
            )
            .size()
            .reset_index(
                name="claim_count"
            )

        )

        return monthly.to_dict(
            orient="records"
        )

    # ==========================================
    # Claim Status Analysis
    # ==========================================

    def claim_status_analysis(self):

        status = (

            self.df[
                "claim_status"
            ]
            .value_counts()
            .reset_index()

        )

        status.columns = [
            "claim_status",
            "count"
        ]

        return status.to_dict(
            orient="records"
        )

    # ==========================================
    # Denial Analysis
    # ==========================================

    def denial_analysis(self):

        denied_df = self.df[
            self.df["claim_status"]
            == "Denied"
        ]

        return {

            "total_denials":
                len(denied_df),

            "denied_amount":
                float(
                    denied_df[
                        "claim_amount"
                    ].sum()
                ),

            "average_denied_amount":
                round(
                    denied_df[
                        "claim_amount"
                    ].mean(),
                    2
                )
        }

    # ==========================================
    # Denial Reasons
    # ==========================================

    def denial_reasons(self):

        reasons = (

            self.df[
                self.df["claim_status"]
                == "Denied"
            ]
            ["denial_reason"]
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
    # Payer Analysis
    # ==========================================

    def payer_analysis(self):

        payer = (

            self.df.groupby(
                "payer_type"
            )
            .agg({

                "claim_amount":
                    "sum",

                "reimbursement_amount":
                    "sum"

            })
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
            )
            .agg({

                "claim_amount":
                    "sum",

                "reimbursement_amount":
                    "sum"

            })
            .reset_index()

        )

        return department.to_dict(
            orient="records"
        )

    # ==========================================
    # Reimbursement Analysis
    # ==========================================

    def reimbursement_analysis(self):

        total_claim_amount = (

            self.df[
                "claim_amount"
            ].sum()

        )

        total_reimbursement = (

            self.df[
                "reimbursement_amount"
            ].sum()

        )

        reimbursement_rate = round(

            (
                total_reimbursement
                /
                total_claim_amount
            )
            * 100,

            2

        )

        return {

            "total_claim_amount":
                float(
                    total_claim_amount
                ),

            "total_reimbursement":
                float(
                    total_reimbursement
                ),

            "reimbursement_rate":
                reimbursement_rate
        }

    # ==========================================
    # Top Denial Reasons
    # ==========================================

    def top_denial_reasons(
            self,
            top_n=10
    ):

        denied = (

            self.df[
                self.df["claim_status"]
                == "Denied"
            ]
            ["denial_reason"]
            .value_counts()
            .head(top_n)
            .reset_index()

        )

        denied.columns = [
            "denial_reason",
            "count"
        ]

        return denied.to_dict(
            orient="records"
        )

    # ==========================================
    # Claims KPIs
    # ==========================================

    def claims_kpis(self):

        total_claims = len(self.df)

        approved = len(
            self.df[
                self.df["claim_status"]
                == "Approved"
            ]
        )

        denied = len(
            self.df[
                self.df["claim_status"]
                == "Denied"
            ]
        )

        total_claim_amount = (

            self.df[
                "claim_amount"
            ].sum()

        )

        reimbursement_amount = (

            self.df[
                "reimbursement_amount"
            ].sum()

        )

        avg_claim_amount = round(

            self.df[
                "claim_amount"
            ].mean(),

            2

        )

        avg_reimbursement = round(

            self.df[
                "reimbursement_amount"
            ].mean(),

            2

        )

        return {

            "total_claims":
                total_claims,

            "total_claim_amount":
                float(
                    total_claim_amount
                ),

            "average_claim_amount":
                avg_claim_amount,

            "approved_claims":
                approved,

            "denied_claims":
                denied,

            "approval_rate":
                round(
                    (
                        approved
                        /
                        total_claims
                    ) * 100,
                    2
                ),

            "denial_rate":
                round(
                    (
                        denied
                        /
                        total_claims
                    ) * 100,
                    2
                ),

            "total_reimbursement":
                float(
                    reimbursement_amount
                ),

            "average_reimbursement":
                avg_reimbursement
        }