from implementations.patient_billing_impl import (
    PatientBillingImplementation
)


class PatientBillingService:

    def __init__(self):

        self.billing_impl = (
            PatientBillingImplementation()
        )

    # ==========================================
    # Billing Summary
    # ==========================================

    def billing_summary(self):

        return (
            self.billing_impl
            .billing_summary()
        )

    # ==========================================
    # Billing Trend
    # ==========================================

    def billing_trend(self):

        return (
            self.billing_impl
            .billing_trend()
        )

    # ==========================================
    # Monthly Billing
    # ==========================================

    def monthly_billing(self):

        return (
            self.billing_impl
            .monthly_billing()
        )

    # ==========================================
    # Billing Status Analysis
    # ==========================================

    def billing_status_analysis(self):

        return (
            self.billing_impl
            .billing_status_analysis()
        )

    # ==========================================
    # Payment Plan Analysis
    # ==========================================

    def payment_plan_analysis(self):

        return (
            self.billing_impl
            .payment_plan_analysis()
        )

    # ==========================================
    # Department Analysis
    # ==========================================

    def department_analysis(self):

        return (
            self.billing_impl
            .department_analysis()
        )

    # ==========================================
    # Payer Analysis
    # ==========================================

    def payer_analysis(self):

        return (
            self.billing_impl
            .payer_analysis()
        )

    # ==========================================
    # Outstanding Balances
    # ==========================================

    def outstanding_balances(self):

        return (
            self.billing_impl
            .outstanding_balances()
        )

    # ==========================================
    # Collection Analysis
    # ==========================================

    def collection_analysis(self):

        return (
            self.billing_impl
            .collection_analysis()
        )

    # ==========================================
    # Payment Plan Performance
    # ==========================================

    def payment_plan_performance(self):

        return (
            self.billing_impl
            .payment_plan_performance()
        )

    # ==========================================
    # Top Outstanding Patients
    # ==========================================

    def top_outstanding_patients(
            self,
            top_n=20
    ):

        return (
            self.billing_impl
            .top_outstanding_patients(top_n)
        )

    # ==========================================
    # Billing KPIs
    # ==========================================

    def billing_kpis(self):

        return (
            self.billing_impl
            .billing_kpis()
        )