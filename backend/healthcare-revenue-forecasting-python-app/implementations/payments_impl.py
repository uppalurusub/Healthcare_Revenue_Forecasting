import pandas as pd

from utils.data_loader import DataLoader


class PaymentsImplementation:

    def __init__(self):

        self.df = DataLoader.load_payments()

        self.df["payment_date"] = pd.to_datetime(
            self.df["payment_date"]
        )

    # ==========================================
    # Payment Summary
    # ==========================================

    def payment_summary(self):

        return {

            "total_payments":
                float(
                    self.df[
                        "total_payment"
                    ].sum()
                ),

            "insurance_payments":
                float(
                    self.df[
                        "insurance_payment"
                    ].sum()
                ),

            "patient_payments":
                float(
                    self.df[
                        "patient_payment"
                    ].sum()
                ),

            "average_payment":
                round(
                    self.df[
                        "total_payment"
                    ].mean(),
                    2
                ),

            "average_days_to_payment":
                round(
                    self.df[
                        "days_to_payment"
                    ].mean(),
                    2
                )
        }

    # ==========================================
    # Payment Trend
    # ==========================================

    def payment_trend(self):

        trend = (

            self.df.groupby(
                "payment_date"
            )["total_payment"]
            .sum()
            .reset_index()

        )

        return trend.to_dict(
            orient="records"
        )

    # ==========================================
    # Monthly Payments
    # ==========================================

    def monthly_payments(self):

        monthly = (

            self.df.groupby(
                pd.Grouper(
                    key="payment_date",
                    freq="ME"
                )
            )["total_payment"]
            .sum()
            .reset_index()

        )

        return monthly.to_dict(
            orient="records"
        )

    # ==========================================
    # Payment Status Analysis
    # ==========================================

    def payment_status_analysis(self):

        status = (

            self.df[
                "payment_status"
            ]
            .value_counts()
            .reset_index()

        )

        status.columns = [
            "payment_status",
            "count"
        ]

        return status.to_dict(
            orient="records"
        )

    # ==========================================
    # Insurance Payments
    # ==========================================

    def insurance_payments(self):

        payer = (

            self.df.groupby(
                "payer_type"
            )["insurance_payment"]
            .sum()
            .reset_index()

        )

        return payer.to_dict(
            orient="records"
        )

    # ==========================================
    # Patient Payments
    # ==========================================

    def patient_payments(self):

        patient = (

            self.df.groupby(
                "payer_type"
            )["patient_payment"]
            .sum()
            .reset_index()

        )

        return patient.to_dict(
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

                "total_payment":
                    "sum",

                "insurance_payment":
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
    # Payment Method Analysis
    # ==========================================

    def payment_method_analysis(self):

        methods = (

            self.df.groupby(
                "payment_method"
            )["total_payment"]
            .sum()
            .reset_index()

        )

        return methods.to_dict(
            orient="records"
        )

    # ==========================================
    # Collection Analysis
    # ==========================================

    def collection_analysis(self):

        billed = (

            self.df[
                "billed_amount"
            ].sum()

        )

        collected = (

            self.df[
                "total_payment"
            ].sum()

        )

        collection_rate = round(

            (
                collected
                /
                billed
            ) * 100,

            2

        )

        return {

            "total_billed":
                float(billed),

            "total_collected":
                float(collected),

            "collection_rate":
                collection_rate
        }

    # ==========================================
    # Days To Payment
    # ==========================================

    def days_to_payment_analysis(self):

        return {

            "average_days":
                round(
                    self.df[
                        "days_to_payment"
                    ].mean(),
                    2
                ),

            "minimum_days":
                int(
                    self.df[
                        "days_to_payment"
                    ].min()
                ),

            "maximum_days":
                int(
                    self.df[
                        "days_to_payment"
                    ].max()
                )
        }

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
            )["total_payment"]
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
    # Payment KPIs
    # ==========================================

    def payment_kpis(self):

        total_payment = (

            self.df[
                "total_payment"
            ].sum()

        )

        insurance_payment = (

            self.df[
                "insurance_payment"
            ].sum()

        )

        patient_payment = (

            self.df[
                "patient_payment"
            ].sum()

        )

        billed_amount = (

            self.df[
                "billed_amount"
            ].sum()

        )

        collection_rate = round(

            (
                total_payment
                /
                billed_amount
            ) * 100,

            2

        )

        payment_success_rate = round(

            (
                len(
                    self.df[
                        self.df[
                            "payment_status"
                        ]
                        .isin(
                            [
                                "Paid",
                                "Partial Paid"
                            ]
                        )
                    ]
                )
                /
                len(self.df)
            ) * 100,

            2

        )

        return {

            "total_payments":
                float(
                    total_payment
                ),

            "insurance_payments":
                float(
                    insurance_payment
                ),

            "patient_payments":
                float(
                    patient_payment
                ),

            "collection_rate":
                collection_rate,

            "insurance_payment_pct":
                round(
                    (
                        insurance_payment
                        /
                        total_payment
                    ) * 100,
                    2
                ),

            "patient_payment_pct":
                round(
                    (
                        patient_payment
                        /
                        total_payment
                    ) * 100,
                    2
                ),

            "average_days_to_payment":
                round(
                    self.df[
                        "days_to_payment"
                    ].mean(),
                    2
                ),

            "payment_success_rate":
                payment_success_rate
        }