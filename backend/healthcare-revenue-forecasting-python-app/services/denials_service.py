from implementations.denials_impl import (
    DenialsImplementation
)


class DenialsService:

    def __init__(self):

        self.denials_impl = (
            DenialsImplementation()
        )

    # ==========================================
    # Denial Summary
    # ==========================================

    def denial_summary(self):

        return (
            self.denials_impl
            .denial_summary()
        )

    # ==========================================
    # Denial Trend
    # ==========================================

    def denial_trend(self):

        return (
            self.denials_impl
            .denial_trend()
        )

    # ==========================================
    # Monthly Denials
    # ==========================================

    def monthly_denials(self):

        return (
            self.denials_impl
            .monthly_denials()
        )

    # ==========================================
    # Denial Reasons
    # ==========================================

    def denial_reasons(self):

        return (
            self.denials_impl
            .denial_reasons()
        )

    # ==========================================
    # Denial Categories
    # ==========================================

    def denial_categories(self):

        return (
            self.denials_impl
            .denial_categories()
        )

    # ==========================================
    # Department Analysis
    # ==========================================

    def department_analysis(self):

        return (
            self.denials_impl
            .department_analysis()
        )

    # ==========================================
    # Payer Analysis
    # ==========================================

    def payer_analysis(self):

        return (
            self.denials_impl
            .payer_analysis()
        )

    # ==========================================
    # Appeal Analysis
    # ==========================================

    def appeal_analysis(self):

        return (
            self.denials_impl
            .appeal_analysis()
        )

    # ==========================================
    # Recovery Analysis
    # ==========================================

    def recovery_analysis(self):

        return (
            self.denials_impl
            .recovery_analysis()
        )

    # ==========================================
    # Resolution Analysis
    # ==========================================

    def resolution_analysis(self):

        return (
            self.denials_impl
            .resolution_analysis()
        )

    # ==========================================
    # Top Denial Reasons
    # ==========================================

    def top_denial_reasons(
            self,
            top_n=10
    ):

        return (
            self.denials_impl
            .top_denial_reasons(top_n)
        )

    # ==========================================
    # Revenue Leakage
    # ==========================================

    def revenue_leakage(self):

        return (
            self.denials_impl
            .revenue_leakage()
        )

    # ==========================================
    # Denial KPIs
    # ==========================================

    def denial_kpis(self):

        return (
            self.denials_impl
            .denial_kpis()
        )