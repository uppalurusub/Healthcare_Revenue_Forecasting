import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DenialVisualization:

    # ==========================================
    # Monthly Denial Trend
    # ==========================================

    @staticmethod
    def denial_trend(df):

        denial_monthly = (

            df.groupby(
                pd.Grouper(
                    key="denial_date",
                    freq="ME"
                )
            )
            .size()
            .reset_index(name="denial_count")

        )

        plt.figure(figsize=(12, 6))

        sns.lineplot(
            data=denial_monthly,
            x="denial_date",
            y="denial_count"
        )

        plt.title("Monthly Denial Trend")

        plt.xlabel("Month")
        plt.ylabel("Denial Count")

        plt.tight_layout()

        return plt

    # ==========================================
    # Denials by Reason
    # ==========================================

    @staticmethod
    def denial_reason_analysis(df):

        reason_df = (

            df["denial_reason"]
            .value_counts()
            .reset_index()

        )

        reason_df.columns = [
            "denial_reason",
            "count"
        ]

        plt.figure(figsize=(12, 6))

        sns.barplot(
            data=reason_df,
            x="denial_reason",
            y="count"
        )

        plt.xticks(rotation=45)

        plt.title(
            "Denials by Reason"
        )

        plt.tight_layout()

        return plt

    # ==========================================
    # Denials by Category
    # ==========================================

    @staticmethod
    def denial_category_analysis(df):

        category_df = (

            df["denial_category"]
            .value_counts()
            .reset_index()

        )

        category_df.columns = [
            "denial_category",
            "count"
        ]

        plt.figure(figsize=(10, 6))

        sns.barplot(
            data=category_df,
            x="denial_category",
            y="count"
        )

        plt.title(
            "Denial Category Analysis"
        )

        plt.tight_layout()

        return plt

    # ==========================================
    # Department Denials
    # ==========================================

    @staticmethod
    def department_denials(df):

        department_df = (

            df.groupby("department")
            .size()
            .reset_index(name="denial_count")

        )

        plt.figure(figsize=(12, 6))

        sns.barplot(
            data=department_df,
            x="department",
            y="denial_count"
        )

        plt.xticks(rotation=45)

        plt.title(
            "Department-wise Denials"
        )

        plt.tight_layout()

        return plt

    # ==========================================
    # Payer Denials
    # ==========================================

    @staticmethod
    def payer_denials(df):

        payer_df = (

            df.groupby("payer_type")
            .size()
            .reset_index(name="denial_count")

        )

        plt.figure(figsize=(10, 6))

        sns.barplot(
            data=payer_df,
            x="payer_type",
            y="denial_count"
        )

        plt.xticks(rotation=30)

        plt.title(
            "Payer-wise Denials"
        )

        plt.tight_layout()

        return plt

    # ==========================================
    # Denied Amount by Payer
    # ==========================================

    @staticmethod
    def denied_amount_by_payer(df):

        payer_amount = (

            df.groupby("payer_type")
            ["claim_amount"]
            .sum()
            .reset_index()

        )

        plt.figure(figsize=(10, 6))

        sns.barplot(
            data=payer_amount,
            x="payer_type",
            y="claim_amount"
        )

        plt.title(
            "Denied Amount by Payer"
        )

        plt.tight_layout()

        return plt

    # ==========================================
    # Recovery Analysis
    # ==========================================

    @staticmethod
    def recovery_analysis(df):

        recovery_df = (

            df.groupby("appeal_status")
            ["recovered_amount"]
            .sum()
            .reset_index()

        )

        plt.figure(figsize=(10, 6))

        sns.barplot(
            data=recovery_df,
            x="appeal_status",
            y="recovered_amount"
        )

        plt.title(
            "Recovered Revenue by Appeal Status"
        )

        plt.tight_layout()

        return plt

    # ==========================================
    # Resolution Time Analysis
    # ==========================================

    @staticmethod
    def resolution_time(df):

        plt.figure(figsize=(10, 6))

        sns.histplot(
            df["days_to_resolution"],
            kde=True
        )

        plt.title(
            "Denial Resolution Time"
        )

        plt.xlabel(
            "Days to Resolution"
        )

        plt.tight_layout()

        return plt

    # ==========================================
    # Recovery Distribution
    # ==========================================

    @staticmethod
    def recovery_distribution(df):

        plt.figure(figsize=(10, 6))

        sns.histplot(
            df["recovered_amount"],
            kde=True
        )

        plt.title(
            "Recovered Revenue Distribution"
        )

        plt.tight_layout()

        return plt

    # ==========================================
    # Correlation Heatmap
    # ==========================================

    @staticmethod
    def denial_correlation(df):

        numeric_df = df.select_dtypes(
            include="number"
        )

        plt.figure(figsize=(10, 8))

        sns.heatmap(
            numeric_df.corr(),
            annot=True,
            fmt=".2f"
        )

        plt.title(
            "Denial Analytics Correlation"
        )

        plt.tight_layout()

        return plt