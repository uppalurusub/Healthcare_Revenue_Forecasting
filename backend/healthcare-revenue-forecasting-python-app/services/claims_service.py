from implementations.claims_impl import (
    ClaimsImplementation
)


class ClaimsService:

    def __init__(self):

        self.claims_impl = (
            ClaimsImplementation()
        )

    # ==========================================
    # Claims Summary
    # ==========================================

    def claims_summary(self):

        return (
            self.claims_impl
            .claims_summary()
        )

    # ==========================================
    # Claims Trend
    # ==========================================

    def claims_trend(self):

        return (
            self.claims_impl
            .claims_trend()
        )

    # ==========================================
    # Monthly Claims
    # ==========================================

    def monthly_claims(self):

        return (
            self.claims_impl
            .monthly_claims()
        )

    # ==========================================
    # Claim Status Analysis
    # ==========================================

    def claim_status_analysis(self):

        return (
            self.claims_impl
            .claim_status_analysis()
        )

    # ==========================================
    # Denial Analysis
    # ==========================================

    def denial_analysis(self):

        return (
            self.claims_impl
            .denial_analysis()
        )

    # ==========================================
    # Denial Reasons
    # ==========================================

    def denial_reasons(self):

        return (
            self.claims_impl
            .denial_reasons()
        )

    # ==========================================
    # Payer Analysis
    # ==========================================

    def payer_analysis(self):

        return (
            self.claims_impl
            .payer_analysis()
        )

    # ==========================================
    # Department Analysis
    # ==========================================

    def department_analysis(self):

        return (
            self.claims_impl
            .department_analysis()
        )

    # ==========================================
    # Reimbursement Analysis
    # ==========================================

    def reimbursement_analysis(self):

        return (
            self.claims_impl
            .reimbursement_analysis()
        )

    # ==========================================
    # Top Denial Reasons
    # ==========================================

    def top_denial_reasons(
            self,
            top_n=10
    ):

        return (
            self.claims_impl
            .top_denial_reasons(top_n)
        )

    # ==========================================
    # Claims KPIs
    # ==========================================

    def claims_kpis(self):

        return (
            self.claims_impl
            .claims_kpis()
        )