from implementations.payments_impl import (
    PaymentsImplementation
)


class PaymentsService:

    def __init__(self):

        self.payments_impl = (
            PaymentsImplementation()
        )

    # ==========================================
    # Payment Summary
    # ==========================================

    def payment_summary(self):

        return (
            self.payments_impl
            .payment_summary()
        )

    # ==========================================
    # Payment Trend
    # ==========================================

    def payment_trend(self):

        return (
            self.payments_impl
            .payment_trend()
        )

    # ==========================================
    # Monthly Payments
    # ==========================================

    def monthly_payments(self):

        return (
            self.payments_impl
            .monthly_payments()
        )

    # ==========================================
    # Payment Status Analysis
    # ==========================================

    def payment_status_analysis(self):

        return (
            self.payments_impl
            .payment_status_analysis()
        )

    # ==========================================
    # Insurance Payments
    # ==========================================

    def insurance_payments(self):

        return (
            self.payments_impl
            .insurance_payments()
        )

    # ==========================================
    # Patient Payments
    # ==========================================

    def patient_payments(self):

        return (
            self.payments_impl
            .patient_payments()
        )

    # ==========================================
    # Payer Analysis
    # ==========================================

    def payer_analysis(self):

        return (
            self.payments_impl
            .payer_analysis()
        )

    # ==========================================
    # Payment Method Analysis
    # ==========================================

    def payment_method_analysis(self):

        return (
            self.payments_impl
            .payment_method_analysis()
        )

    # ==========================================
    # Collection Analysis
    # ==========================================

    def collection_analysis(self):

        return (
            self.payments_impl
            .collection_analysis()
        )

    # ==========================================
    # Days To Payment Analysis
    # ==========================================

    def days_to_payment_analysis(self):

        return (
            self.payments_impl
            .days_to_payment_analysis()
        )

    # ==========================================
    # Top Payers
    # ==========================================

    def top_payers(
            self,
            top_n=10
    ):

        return (
            self.payments_impl
            .top_payers(top_n)
        )

    # ==========================================
    # Payment KPIs
    # ==========================================

    def payment_kpis(self):

        return (
            self.payments_impl
            .payment_kpis()
        )