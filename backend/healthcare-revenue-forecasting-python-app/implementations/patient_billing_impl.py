import pandas as pd

from utils.data_loader import DataLoader


class PatientBillingImplementation:

    def __init__(self):

        self.df = DataLoader.load_patient_billing()

        self.df["bill_date"] = pd.to_datetime(
            self.df["bill_date"]
        )

    # ==========================================
    # Billing Summary
    # ==========================================

    def billing_summary(self):

        return {

            "total_chargess":
                float(
                    self.df[
                        "total_charges"
                    ].sum()
                ),

            "insurance_responsibility":
                float(
                    self.df[
                        "insurance_responsibility"
                    ].sum()
                ),

            "patient_responsibility":
                float(
                    self.df[
                        "patient_responsibility"
                    ].sum()
                ),

            "patient_payment":
                float(
                    self.df[
                        "patient_payment"
                    ].sum()
                ),

            "remaining_balance":
                float(
                    self.df[
                        "remaining_balance"
                    ].sum()
                )
        }

    # ==========================================
    # Billing Trend
    # ==========================================

    def billing_trend(self):

        trend = (

            self.df.groupby(
                "bill_date"
            )["total_charges"]
            .sum()
            .reset_index()

        )

        return trend.to_dict(
            orient="records"
        )

    # ==========================================
    # Monthly Billing Trend
    # ==========================================

    def monthly_billing(self):

        monthly = (

            self.df.groupby(
                pd.Grouper(
                    key="bill_date",
                    freq="ME"
                )
            )["total_charges"]
            .sum()
            .reset_index()

        )

        return monthly.to_dict(
            orient="records"
        )

    # ==========================================
    # Billing Status Analysis
    # ==========================================

    def billing_status_analysis(self):

        status = (

            self.df[
                "billing_status"
            ]
            .value_counts()
            .reset_index()

        )

        status.columns = [
            "billing_status",
            "count"
        ]

        return status.to_dict(
            orient="records"
        )

    # ==========================================
    # Payment Plan Analysis
    # ==========================================

    def payment_plan_analysis(self):

        plans = (

            self.df[
                "payment_plan"
            ]
            .value_counts()
            .reset_index()

        )

        plans.columns = [
            "payment_plan",
            "count"
        ]

        return plans.to_dict(
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

                "total_charges":
                    "sum",

                "patient_payment":
                    "sum",

                "remaining_balance":
                    "sum"

            })
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
            )
            .agg({

                "total_charges":
                    "sum",

                "insurance_responsibility":
                    "sum",

                "patient_payment":
                    "sum"

            })
            .reset_index()

        )

        return payer.to_dict(
            orient="records"
        )

    # ==========================================
    # Outstanding Balances
    # ==========================================

    def outstanding_balances(self):

        balances = (

            self.df.sort_values(
                by="remaining_balance",
                ascending=False
            )
            .head(50)

        )

        return balances.to_dict(
            orient="records"
        )

    # ==========================================
    # Collection Analysis
    # ==========================================

    def collection_analysis(self):

        responsibility = (

            self.df[
                "patient_responsibility"
            ].sum()

        )

        collected = (

            self.df[
                "patient_payment"
            ].sum()

        )

        collection_rate = round(

            (
                collected
                /
                responsibility
            ) * 100,

            2

        ) if responsibility > 0 else 0

        return {

            "patient_responsibility":
                float(
                    responsibility
                ),

            "patient_collected":
                float(
                    collected
                ),

            "collection_rate":
                collection_rate
        }

    # ==========================================
    # Payment Plan Performance
    # ==========================================

    def payment_plan_performance(self):

        performance = (

            self.df.groupby(
                "payment_plan"
            )
            .agg({

                "patient_payment":
                    "sum",

                "remaining_balance":
                    "sum"

            })
            .reset_index()

        )

        return performance.to_dict(
            orient="records"
        )

    # ==========================================
    # Top Outstanding Patients
    # ==========================================

    def top_outstanding_patients(
            self,
            top_n=20
    ):

        patients = (

            self.df.groupby(
                "patient_id"
            )["remaining_balance"]
            .sum()
            .sort_values(
                ascending=False
            )
            .head(top_n)
            .reset_index()

        )

        return patients.to_dict(
            orient="records"
        )

    # ==========================================
    # Billing KPIs
    # ==========================================

    def billing_kpis(self):

        total_charges = (
            self.df[
                "total_charges"
            ].sum()
        )

        insurance_responsibility = (
            self.df[
                "insurance_responsibility"
            ].sum()
        )

        patient_responsibility = (
            self.df[
                "patient_responsibility"
            ].sum()
        )

        patient_payment = (
            self.df[
                "patient_payment"
            ].sum()
        )

        remaining_balance = (
            self.df[
                "remaining_balance"
            ].sum()
        )

        collection_rate = round(

            (
                patient_payment
                /
                patient_responsibility
            ) * 100,

            2

        ) if patient_responsibility > 0 else 0

        payment_plan_rate = round(

            (
                len(
                    self.df[
                        self.df[
                            "payment_plan"
                        ] == "Yes"
                    ]
                )
                /
                len(self.df)
            ) * 100,

            2

        )

        return {

            "total_chargess":
                float(
                    total_charges
                ),

            "insurance_responsibility":
                float(
                    insurance_responsibility
                ),

            "patient_responsibility":
                float(
                    patient_responsibility
                ),

            "patient_payment":
                float(
                    patient_payment
                ),

            "remaining_balance":
                float(
                    remaining_balance
                ),

            "collection_rate":
                collection_rate,

            "payment_plan_rate":
                payment_plan_rate
        }