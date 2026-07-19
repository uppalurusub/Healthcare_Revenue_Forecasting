from implementations.revenue_impl import (
    RevenueImplementation
)

from visualizations.revenue_viz import (
    RevenueVisualization
)


class RevenueService:

    def __init__(self):

        self.revenue_impl = (
            RevenueImplementation()
        )

    # ==========================================
    # Revenue Summary
    # ==========================================

    def revenue_summary(self):

        return (
            self.revenue_impl
            .revenue_summary()
        )

    # ==========================================
    # Revenue Trend
    # ==========================================

    def revenue_trend(self):

        return (
            self.revenue_impl
            .revenue_trend()
        )

    # ==========================================
    # Monthly Revenue
    # ==========================================

    def monthly_revenue(self):

        return (
            self.revenue_impl
            .monthly_revenue()
        )

    def monthly_revenue_chart(self):

        df = (
            self.revenue_impl
            .monthly_revenue_chart()
            
        )

        return (
            RevenueVisualization
            .monthly_revenue_chart(df)
        )
    # ==========================================
    # Revenue by Department
    # ==========================================

    def revenue_by_department(self):

        return (
            self.revenue_impl
            .revenue_by_department()
        )

    def revenue_by_department_chart(self):

        df = (
            self.revenue_impl
            .revenue_by_department_chart()
            
        )

        return (
            RevenueVisualization
            .revenue_by_department_chart(df)
        )


    # ==========================================
    # Revenue by Payer
    # ==========================================

    def revenue_by_payer(self):

        return (
            self.revenue_impl
            .revenue_by_payer()
        )
    
    def revenue_by_payer_chart(self):

        df = (
            self.revenue_impl
            .revenue_by_payer_chart()
            
        )

        return (
            RevenueVisualization
            .revenue_by_payer_chart(df)
        )

    
    
    

    # ==========================================
    # Revenue Leakage
    # ==========================================

    def revenue_leakage(self):

        return (
            self.revenue_impl
            .revenue_leakage()
        )
    
    
    # ==========================================
    # Reimbursement Analysis
    # ==========================================

    def reimbursement_analysis(self):

        return (
            self.revenue_impl
            .reimbursement_analysis()
        )

    # ==========================================
    # Top Departments
    # ==========================================

    def top_departments(
            self,
            top_n=10
    ):

        return (
            self.revenue_impl
            .top_departments(top_n)
        )
    
    def top_departments_chart(
            self,
            top_n=10
    ):

        df = (
            self.revenue_impl
            .top_departments_chart()
            
        )

        return (
            RevenueVisualization
            .top_departments_chart(df)
        )

    # ==========================================
    # Top Payers
    # ==========================================

    def top_payers(
            self,
            top_n=10
    ):

        return (
            self.revenue_impl
            .top_payers(top_n)
        )

    def top_payers_chart(
            self,
            top_n=10
    ):

        df = (
            self.revenue_impl
            .top_payers_chart()
            
        )

        return (
            RevenueVisualization
            .top_payers_chart(df)
        )
    
    # ==========================================
    # Revenue KPIs
    # ==========================================

    def revenue_kpis(self):

        return (
            self.revenue_impl
            .revenue_kpis()
        )
    

    def revenue_distribution_chart(self):

        return (
            self.revenue_impl
            .revenue_distribution_chart()
        )
    
    def revenue_boxplot_chart(self):

        return (
            self.revenue_impl
            .revenue_boxplot_chart()
        )
    
    def revenue_vs_collections_chart(self):

        return (
            self.revenue_impl
            .revenue_vs_collections_chart()
        )
    
    def correlation_heatmap_chart(self):

        return (
            self.revenue_impl
            .correlation_heatmap_chart()
        )
