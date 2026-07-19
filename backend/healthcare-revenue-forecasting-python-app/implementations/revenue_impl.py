from utils.data_loader import DataLoader
from utils.preprocessing import (
    RevenueFeatureEngineering
)
import pandas as pd

from utils.metrics import (
    RevenueMetrics
)

from visualizations.revenue_viz import RevenueVisualization



class RevenueImplementation:

    def __init__(self):

        self.df = DataLoader.load_revenue()

    # ==========================================
    # Revenue Summary
    # ==========================================

    def revenue_summary(self):

        return {

            "total_revenue":
                RevenueMetrics.total_revenue(
                    self.df
                ),

            "average_revenue":
                RevenueMetrics.average_revenue(
                    self.df
                ),

            "collection_rate":
                RevenueMetrics.collection_rate(
                    self.df
                ),

            "reimbursement_rate":
                RevenueMetrics.reimbursement_rate(
                    self.df
                ),

            "revenue_leakage":
                RevenueMetrics.revenue_leakage(
                    self.df
                )
        }

    # ==========================================
    # Revenue Trend
    # ==========================================

    def revenue_trend(self):

        trend = (

            self.df
            .groupby(
                self.df["service_date"]
            )["gross_revenue"]
            .sum()
            .reset_index()

        )

        return trend.to_dict(
            orient="records"
        )

    # ==========================================
    # Monthly Revenue Trend
    # ==========================================

    def monthly_revenue(self):

        self.df["service_date"] = (
            self.df["service_date"]
            .astype("datetime64[ns]")
        )

        monthly = (

            self.df.groupby(
                pd.Grouper(
                    key="service_date",
                    freq="ME"
                )
            )["gross_revenue"]
            .sum()
            .reset_index()

        )

        #return monthly
        return monthly.to_dict(
            orient="records"
        )
    
    def monthly_revenue_chart(self):

        self.df["service_date"] = (
            self.df["service_date"]
            .astype("datetime64[ns]")
        )

        monthly = (

            self.df.groupby(
                pd.Grouper(
                    key="service_date",
                    freq="ME"
                )
            )["gross_revenue"]
            .sum()
            .reset_index()

        )

        return monthly
        
    # ==========================================
    # Revenue by Department
    # ==========================================

    def revenue_by_department(self):

        department = (

            self.df.groupby(
                "department"
            )["gross_revenue"]
            .sum()
            .sort_values(
                ascending=False
            )
            .reset_index()

        )

        return department.to_dict(
            orient="records"
        )
    
    def revenue_by_department_chart(self):

        department = (

            self.df.groupby(
                "department"
            )["gross_revenue"]
            .sum()
            .sort_values(
                ascending=False
            )
            .reset_index()

        )

        return department

    # ==========================================
    # Revenue by Payer
    # ==========================================

    def revenue_by_payer(self):

        payer = (

            self.df.groupby(
                "payer_type"
            )["gross_revenue"]
            .sum()
            .sort_values(
                ascending=False
            )
            .reset_index()

        )

        return payer.to_dict(
            orient="records"
        )
    
    def revenue_by_payer_chart(self):

        payer = (

            self.df.groupby(
                "payer_type"
            )["gross_revenue"]
            .sum()
            .sort_values(
                ascending=False
            )
            .reset_index()

        )

        return payer

    # ==========================================
    # Collection Analysis
    # ==========================================

    def collection_analysis(self):

        total_collections = (

            self.df[
                "payments_collected"
            ].sum()

        )

        collection_rate = (

            RevenueMetrics.collection_rate(
                self.df
            )

        )

        return {

            "total_collections":
                float(
                    total_collections
                ),

            "collection_rate":
                collection_rate
        }

    # ==========================================
    # Revenue Leakage
    # ==========================================

    def revenue_leakage(self):

        leakage_df = (

            RevenueFeatureEngineering
            .revenue_leakage(
                self.df.copy()
            )

        )

        leakage = (

            leakage_df[
                "revenue_leakage"
            ]
            .sum()

        )

        return {

            "revenue_leakage":
                float(leakage)
        }

    # ==========================================
    # Reimbursement Analysis
    # ==========================================

    def reimbursement_analysis(self):

        total_expected = (

            self.df[
                "expected_reimbursement"
            ].sum()

        )

        total_collected = (

            self.df[
                "payments_collected"
            ].sum()

        )

        reimbursement_rate = (

            RevenueMetrics
            .reimbursement_rate(
                self.df
            )

        )

        return {

            "expected_reimbursement":
                float(
                    total_expected
                ),

            "payments_collected":
                float(
                    total_collected
                ),

            "reimbursement_rate":
                reimbursement_rate
        }

    # ==========================================
    # Top Revenue Departments
    # ==========================================

    def top_departments(
            self,
            top_n=10
    ):

        df = (

            self.df.groupby(
                "department"
            )["gross_revenue"]
            .sum()
            .sort_values(
                ascending=False
            )
            .head(top_n)
            .reset_index()

        )

        return df.to_dict(
            orient="records"
        )
    
    
    def top_departments_chart(
            self,
            top_n=10
    ):

        df = (

            self.df.groupby(
                "department"
            )["gross_revenue"]
            .sum()
            .sort_values(
                ascending=False
            )
            .head(top_n)
            .reset_index()

        )

        return df

    # ==========================================
    # Top Payers
    # ==========================================

    def top_payers(
            self,
            top_n=10
    ):

        df = (

            self.df.groupby(
                "payer_type"
            )["gross_revenue"]
            .sum()
            .sort_values(
                ascending=False
            )
            .head(top_n)
            .reset_index()

        )

        return df.to_dict(
            orient="records"
        )
    
    def top_payers_chart(
            self,
            top_n=10
    ):

        df = (

            self.df.groupby(
                "payer_type"
            )["gross_revenue"]
            .sum()
            .sort_values(
                ascending=False
            )
            .head(top_n)
            .reset_index()

        )

        return df

    # ==========================================
    # Revenue KPIs
    # ==========================================

    def revenue_kpis(self):

        return {

            "total_revenue":
                RevenueMetrics.total_revenue(
                    self.df
                ),

            "average_revenue":
                RevenueMetrics.average_revenue(
                    self.df
                ),

            "collection_rate":
                RevenueMetrics.collection_rate(
                    self.df
                ),

            "reimbursement_rate":
                RevenueMetrics.reimbursement_rate(
                    self.df
                ),

            "revenue_leakage":
                RevenueMetrics.revenue_leakage(
                    self.df
                )
        }
    
    
    def revenue_distribution_chart(self):
        return (
            RevenueVisualization
            .revenue_distribution_chart(self.df)
        )
    
    def revenue_boxplot_chart(self):
        return (
            RevenueVisualization
            .revenue_boxplot_chart(self.df)
        )
    
    def revenue_vs_collections_chart(self):
        return (
            RevenueVisualization
            .revenue_vs_collections_chart(self.df)
        )

    def correlation_heatmap_chart(self):
        return (
            RevenueVisualization
            .correlation_heatmap_chart(self.df)
        )

    

    