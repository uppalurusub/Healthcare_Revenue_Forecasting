from implementations.ar_aging_impl import (
    ARAgingImplementation
)


class ARAgingService:

    def __init__(self):

        self.ar_impl = (
            ARAgingImplementation()
        )

    # ==========================================
    # AR Summary
    # ==========================================

    def ar_summary(self):

        return (
            self.ar_impl
            .ar_summary()
        )

    # ==========================================
    # AR Trend
    # ==========================================

    def ar_trend(self):

        return (
            self.ar_impl
            .ar_trend()
        )

    # ==========================================
    # Monthly AR
    # ==========================================

    def monthly_ar(self):

        return (
            self.ar_impl
            .monthly_ar()
        )

    # ==========================================
    # Aging Bucket Analysis
    # ==========================================

    def aging_bucket_analysis(self):

        return (
            self.ar_impl
            .aging_bucket_analysis()
        )

    # ==========================================
    # Collection Status Analysis
    # ==========================================

    def collection_status_analysis(self):

        return (
            self.ar_impl
            .collection_status_analysis()
        )

    # ==========================================
    # Risk Analysis
    # ==========================================

    def risk_analysis(self):

        return (
            self.ar_impl
            .risk_analysis()
        )

    # ==========================================
    # Payer Analysis
    # ==========================================

    def payer_analysis(self):

        return (
            self.ar_impl
            .payer_analysis()
        )

    # ==========================================
    # Department Analysis
    # ==========================================

    def department_analysis(self):

        return (
            self.ar_impl
            .department_analysis()
        )

    # ==========================================
    # Expected Collections
    # ==========================================

    def expected_collections(self):

        return (
            self.ar_impl
            .expected_collections()
        )

    # ==========================================
    # High Risk Accounts
    # ==========================================

    def high_risk_accounts(self):

        return (
            self.ar_impl
            .high_risk_accounts()
        )

    # ==========================================
    # Top Payers
    # ==========================================

    def top_payers(
            self,
            top_n=10
    ):

        return (
            self.ar_impl
            .top_payers(top_n)
        )

    # ==========================================
    # AR KPIs
    # ==========================================

    def ar_kpis(self):

        return (
            self.ar_impl
            .ar_kpis()
        )