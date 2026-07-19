from implementations.revenue_impl import (
    RevenueImplementation
)

from implementations.claims_impl import (
    ClaimsImplementation
)

from implementations.payments_impl import (
    PaymentsImplementation
)

from implementations.denials_impl import (
    DenialsImplementation
)

from implementations.ar_aging_impl import (
    ARAgingImplementation
)

from implementations.patient_billing_impl import (
    PatientBillingImplementation
)

from implementations.forecasting_impl import (
    ForecastingImplementation
)


class DashboardImplementation:

    def __init__(self):

        self.revenue = RevenueImplementation()

        self.claims = ClaimsImplementation()

        self.payments = PaymentsImplementation()

        self.denials = DenialsImplementation()

        self.ar = ARAgingImplementation()

        self.billing = (
            PatientBillingImplementation()
        )

        self.forecasting = (
            ForecastingImplementation()
        )

    # ==========================================
    # Executive Dashboard
    # ==========================================

    def executive_dashboard(self):

        return {

            "revenue":
                self.revenue.revenue_kpis(),

            "claims":
                self.claims.claims_kpis(),

            "payments":
                self.payments.payment_kpis(),

            "denials":
                self.denials.denial_kpis(),

            "ar_aging":
                self.ar.ar_kpis(),

            "patient_billing":
                self.billing.billing_kpis(),

            "forecast":
                self.forecasting.forecast_kpis()
        }

    # ==========================================
    # Executive Summary
    # ==========================================

    def executive_summary(self):

        revenue = (
            self.revenue.revenue_kpis()
        )

        claims = (
            self.claims.claims_kpis()
        )

        denials = (
            self.denials.denial_kpis()
        )

        ar = (
            self.ar.ar_kpis()
        )

        billing = (
            self.billing.billing_kpis()
        )

        forecast = (
            self.forecasting.forecast_kpis()
        )

        return {

            "total_revenue":
                revenue.get(
                    "total_revenue",
                    0
                ),

            "collection_rate":
                revenue.get(
                    "collection_rate",
                    0
                ),

            "denial_rate":
                claims.get(
                    "denial_rate",
                    0
                ),

            "recovery_rate":
                denials.get(
                    "recovery_rate",
                    0
                ),

            "ar_balance":
                ar.get(
                    "total_ar_balance",
                    0
                ),

            "patient_balance":
                billing.get(
                    "remaining_balance",
                    0
                ),

            "projected_revenue":
                forecast.get(
                    "projected_revenue",
                    0
                )
        }

    # ==========================================
    # Revenue Dashboard
    # ==========================================

    def revenue_dashboard(self):

        return {

            "summary":
                self.revenue.revenue_summary(),

            "kpis":
                self.revenue.revenue_kpis(),

            "department_analysis":
                self.revenue.revenue_by_department(),

            "payer_analysis":
                self.revenue.revenue_by_payer(),

            "collection_analysis":
                self.revenue.collection_analysis(),

            "reimbursement_analysis":
                self.revenue.reimbursement_analysis(),

            "revenue_leakage":
                self.revenue.revenue_leakage()
        }

    # ==========================================
    # Claims Dashboard
    # ==========================================

    def claims_dashboard(self):

        return {

            "summary":
                self.claims.claims_summary(),

            "kpis":
                self.claims.claims_kpis(),

            "status":
                self.claims.claim_status_analysis(),

            "denials":
                self.claims.denial_analysis(),

            "payer_analysis":
                self.claims.payer_analysis(),

            "department_analysis":
                self.claims.department_analysis()
        }

    # ==========================================
    # Payments Dashboard
    # ==========================================

    def payments_dashboard(self):

        return {

            "summary":
                self.payments.payment_summary(),

            "kpis":
                self.payments.payment_kpis(),

            "payer_analysis":
                self.payments.payer_analysis(),

            "payment_methods":
                self.payments.payment_method_analysis(),

            "collection_analysis":
                self.payments.collection_analysis()
        }

    # ==========================================
    # Denials Dashboard
    # ==========================================

    def denials_dashboard(self):

        return {

            "summary":
                self.denials.denial_summary(),

            "kpis":
                self.denials.denial_kpis(),

            "reasons":
                self.denials.denial_reasons(),

            "categories":
                self.denials.denial_categories(),

            "appeals":
                self.denials.appeal_analysis(),

            "recovery":
                self.denials.recovery_analysis(),

            "revenue_leakage":
                self.denials.revenue_leakage()
        }

    # ==========================================
    # AR Aging Dashboard
    # ==========================================

    def ar_dashboard(self):

        return {

            "summary":
                self.ar.ar_summary(),

            "kpis":
                self.ar.ar_kpis(),

            "aging_buckets":
                self.ar.aging_bucket_analysis(),

            "risk_analysis":
                self.ar.risk_analysis(),

            "expected_collections":
                self.ar.expected_collections(),

            "high_risk_accounts":
                self.ar.high_risk_accounts()
        }

    # ==========================================
    # Patient Billing Dashboard
    # ==========================================

    def patient_billing_dashboard(self):

        return {

            "summary":
                self.billing.billing_summary(),

            "kpis":
                self.billing.billing_kpis(),

            "collection_analysis":
                self.billing.collection_analysis(),

            "payment_plans":
                self.billing.payment_plan_analysis(),

            "outstanding_balances":
                self.billing.outstanding_balances()
        }

    # ==========================================
    # Forecast Dashboard
    # ==========================================

    def forecast_dashboard(self):

        return {

            "forecast_summary":
                self.forecasting.forecast_summary(),

            "forecast_kpis":
                self.forecasting.forecast_kpis(),

            "revenue_forecast":
                self.forecasting.revenue_forecast(),

            "collection_forecast":
                self.forecasting.collection_forecast(),

            "ar_forecast":
                self.forecasting.ar_forecast(),

            "model_comparison":
                self.forecasting.model_comparison()
        }

    # ==========================================
    # Dashboard KPIs
    # ==========================================

    def dashboard_kpis(self):

        revenue = (
            self.revenue.revenue_kpis()
        )

        claims = (
            self.claims.claims_kpis()
        )

        denials = (
            self.denials.denial_kpis()
        )

        ar = (
            self.ar.ar_kpis()
        )

        billing = (
            self.billing.billing_kpis()
        )

        forecast = (
            self.forecasting.forecast_kpis()
        )

        return {

            "total_revenue":
                revenue.get(
                    "total_revenue",
                    0
                ),

            "collection_rate":
                revenue.get(
                    "collection_rate",
                    0
                ),

            "reimbursement_rate":
                revenue.get(
                    "reimbursement_rate",
                    0
                ),

            "denial_rate":
                claims.get(
                    "denial_rate",
                    0
                ),

            "recovery_rate":
                denials.get(
                    "recovery_rate",
                    0
                ),

            "collection_potential":
                ar.get(
                    "collection_potential",
                    0
                ),

            "patient_collection_rate":
                billing.get(
                    "collection_rate",
                    0
                ),

            "projected_revenue":
                forecast.get(
                    "projected_revenue",
                    0
                ),

            "forecast_accuracy":
                forecast.get(
                    "forecast_accuracy",
                    0
                )
        }
    