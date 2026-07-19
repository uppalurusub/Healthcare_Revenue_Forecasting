import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.data_loader import DataLoader

import io
from fastapi.responses import StreamingResponse
from utils.chart_utils import (
    save_chart_revenue_monthly,
    save_chart_revenue_department,
    save_chart_revenue_payer,
    save_chart_revenue_top_payer,
    save_chart_revenue_top_department,
    save_chart_revenue_distribution,
    save_chart_revenue_box,
    save_chart_revenue_collection,
    save_chart_revenue_correlation
)
class RevenueVisualization:

    def __init__(self):

        self.df = DataLoader.load_revenue()

    # ==========================================
    # Monthly Revenue Trend
    # ==========================================
    @staticmethod
    def monthly_revenue_chart(df):

        plt.figure(figsize=(12, 6))

        sns.lineplot(
            data=df,
            x="service_date",
            y="gross_revenue",
            marker="o"
        )

        plt.title(
            "Monthly Revenue Trend"
        )

        plt.xlabel("Month")

        plt.ylabel("Revenue")

        plt.xticks(rotation=45)

        plt.tight_layout()

        buffer = io.BytesIO()

        plt.savefig(
            buffer,
            format="png"
        )

        save_chart_revenue_monthly(
            "revenue_monthly_chart.png"
        )

        buffer.seek(0)

        plt.close()

        return StreamingResponse(
            buffer,
            media_type="image/png"
        )

    

    # ==========================================
    # Revenue by Department
    # ==========================================

    @staticmethod
    def revenue_by_department_chart(df):

        plt.figure(figsize=(12, 6))

        department_df = (

            df.groupby(
                "department"
            )["gross_revenue"]
            .sum()
            .sort_values(
                ascending=False
            )
            .reset_index()

        )

        plt.figure(figsize=(10, 6))

        sns.barplot(
            data=department_df,
            x="department",
            y="gross_revenue"
        )

        plt.title(
            "Revenue by Department"
        )

        plt.xlabel("Department")

        plt.ylabel("Gross Revenue")


        plt.xticks(rotation=45)

        plt.tight_layout()

        buffer = io.BytesIO()

        plt.savefig(
            buffer,
            format="png"
        )

        save_chart_revenue_department(
            "revenue_department_chart.png"
        )

        buffer.seek(0)

        plt.close()

        return StreamingResponse(
            buffer,
            media_type="image/png"
        )

    # ==========================================
    # Revenue by Payer
    # ==========================================

    @staticmethod
    def revenue_by_payer_chart(df):

        payer_df = (

            df.groupby(
                "payer_type"
            )["gross_revenue"]
            .sum()
            .reset_index()

        )

        plt.figure(figsize=(10, 6))

        sns.barplot(
            data=payer_df,
            x="payer_type",
            y="gross_revenue"
        )

        plt.title(
            "Revenue by Payer"
        )

        plt.xlabel("Payer Type")

        plt.ylabel("Gross Revenue")

        plt.xticks(rotation=30)

        plt.tight_layout()

        buffer = io.BytesIO()

        plt.savefig(
            buffer,
            format="png"
        )

        save_chart_revenue_payer(
            "revenue_payer_chart.png"
        )

        buffer.seek(0)

        plt.close()

        return StreamingResponse(
            buffer,
            media_type="image/png"
        )

    

    

    # ==========================================
    # Revenue Distribution
    # ==========================================

    @staticmethod
    def revenue_distribution_chart(df):

        plt.figure(figsize=(10, 6))

        sns.histplot(
            df["gross_revenue"],
            kde=True
        )

        plt.title(
            "Revenue Distribution"
        )



        plt.tight_layout()

        buffer = io.BytesIO()

        plt.savefig(
            buffer,
            format="png"
        )

        save_chart_revenue_distribution(
            "revenue_distribution_chart.png"
        )

        buffer.seek(0)

        plt.close()

        return StreamingResponse(
            buffer,
            media_type="image/png"
        )
    
    # ==========================================
    # Revenue Boxplot
    # ==========================================

    @staticmethod
    def revenue_boxplot_chart(df):

        plt.figure(figsize=(8, 5))

        sns.boxplot(
            x=df["gross_revenue"]
        )

        plt.title(
            "Revenue Outlier Analysis"
        )

        plt.tight_layout()

        buffer = io.BytesIO()

        plt.savefig(
            buffer,
            format="png"
        )

        save_chart_revenue_box(
            "revenue_box_chart.png"
        )

        buffer.seek(0)

        plt.close()

        return StreamingResponse(
            buffer,
            media_type="image/png"
        )

    # ==========================================
    # Revenue vs Collections
    # ==========================================

    @staticmethod
    def revenue_vs_collections_chart(df):

        plt.figure(figsize=(10, 6))

        sns.scatterplot(
            data=df,
            x="gross_revenue",
            y="payments_collected"
        )

        plt.title(
            "Revenue vs Collections"
        )

        plt.tight_layout()

        buffer = io.BytesIO()

        plt.savefig(
            buffer,
            format="png"
        )

        save_chart_revenue_collection(
            "revenue_collection_chart.png"
        )

        buffer.seek(0)

        plt.close()

        return StreamingResponse(
            buffer,
            media_type="image/png"
        )

    # ==========================================
    # Correlation Heatmap
    # ==========================================

    @staticmethod
    def correlation_heatmap_chart(df):

        numeric_df = df.select_dtypes(
            include="number"
        )

        plt.figure(figsize=(12, 8))

        sns.heatmap(
            numeric_df.corr(),
            annot=True,
            fmt=".2f"
        )

        plt.title(
            "Revenue Correlation Matrix"
        )

        plt.tight_layout()

        buffer = io.BytesIO()

        plt.savefig(
            buffer,
            format="png"
        )

        save_chart_revenue_correlation(
            "revenue_correlation_chart.png"
        )

        buffer.seek(0)

        plt.close()

        return StreamingResponse(
            buffer,
            media_type="image/png"
        )
    

    

    
    @staticmethod
    def top_departments_chart(df):

        payer_df = (

            df.groupby(
                "department"
            )["gross_revenue"]
            .sum()
            .reset_index()

        )

        plt.figure(figsize=(10, 6))

        sns.barplot(
            data=payer_df,
            x="department",
            y="gross_revenue"
        )

        plt.title(
            "Revenue by Top Departments"
        )

        plt.xlabel("Department")

        plt.ylabel("Gross Revenue")

        plt.xticks(rotation=30)

        plt.tight_layout()

        buffer = io.BytesIO()

        plt.savefig(
            buffer,
            format="png"
        )

        save_chart_revenue_top_department(
            "revenue_top_department_chart.png"
        )

        buffer.seek(0)

        plt.close()

        return StreamingResponse(
            buffer,
            media_type="image/png"
        )
    

    @staticmethod
    def top_payers_chart(df):

        payer_df = (

            df.groupby(
                "payer_type"
            )["gross_revenue"]
            .sum()
            .reset_index()

        )

        plt.figure(figsize=(10, 6))

        sns.barplot(
            data=payer_df,
            x="payer_type",
            y="gross_revenue"
        )

        plt.title(
            "Revenue by Top Payer Types"
        )

        plt.xlabel("Payer Type")

        plt.ylabel("Gross Revenue")

        plt.xticks(rotation=30)

        plt.tight_layout()

        buffer = io.BytesIO()

        plt.savefig(
            buffer,
            format="png"
        )

        save_chart_revenue_top_payer(
            "revenue_top_payer_chart.png"
        )

        buffer.seek(0)

        plt.close()

        return StreamingResponse(
            buffer,
            media_type="image/png"
        )