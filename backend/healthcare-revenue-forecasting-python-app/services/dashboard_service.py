from implementations.dashboard_impl import (
    DashboardImplementation
)


class DashboardService:

    def __init__(self):

        self.dashboard_impl = (
            DashboardImplementation()
        )

    # ==========================================
    # Executive Dashboard
    # ==========================================

    def executive_dashboard(self):

        return (
            self.dashboard_impl
            .executive_dashboard()
        )

    # ==========================================
    # Executive Summary
    # ==========================================

    def executive_summary(self):

        return (
            self.dashboard_impl
            .executive_summary()
        )

    # ==========================================
    # Revenue Dashboard
    # ==========================================

    def revenue_dashboard(self):

        return (
            self.dashboard_impl
            .revenue_dashboard()
        )

    # ==========================================
    # Claims Dashboard
    # ==========================================

    def claims_dashboard(self):

        return (
            self.dashboard_impl
            .claims_dashboard()
        )

    # ==========================================
    # Payments Dashboard
    # ==========================================

    def payments_dashboard(self):

        return (
            self.dashboard_impl
            .payments_dashboard()
        )

    # ==========================================
    # Denials Dashboard
    # ==========================================

    def denials_dashboard(self):

        return (
            self.dashboard_impl
            .denials_dashboard()
        )

    # ==========================================
    # AR Aging Dashboard
    # ==========================================

    def ar_dashboard(self):

        return (
            self.dashboard_impl
            .ar_dashboard()
        )

    # ==========================================
    # Patient Billing Dashboard
    # ==========================================

    def patient_billing_dashboard(self):

        return (
            self.dashboard_impl
            .patient_billing_dashboard()
        )

    # ==========================================
    # Forecast Dashboard
    # ==========================================

    def forecast_dashboard(self):

        return (
            self.dashboard_impl
            .forecast_dashboard()
        )

    # ==========================================
    # Dashboard KPIs
    # ==========================================

    def dashboard_kpis(self):

        return (
            self.dashboard_impl
            .dashboard_kpis()
        )