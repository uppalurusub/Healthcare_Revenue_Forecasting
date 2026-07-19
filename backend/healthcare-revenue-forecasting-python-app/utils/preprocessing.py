import pandas as pd
import numpy as np

from sklearn.preprocessing import (
    LabelEncoder,
    StandardScaler,
    MinMaxScaler
)


class Preprocessing:

    # ==========================================
    # Missing Values
    # ==========================================

    @staticmethod
    def missing_value_report(df):

        report = pd.DataFrame({
            "missing_count": df.isnull().sum(),
            "missing_pct":
                round(
                    (df.isnull().sum() / len(df)) * 100,
                    2
                )
        })

        return report.sort_values(
            by="missing_pct",
            ascending=False
        )

    @staticmethod
    def fill_numeric_median(df):

        numeric_cols = df.select_dtypes(
            include=np.number
        ).columns

        for col in numeric_cols:
            df[col] = df[col].fillna(
                df[col].median()
            )

        return df

    @staticmethod
    def fill_categorical_mode(df):

        cat_cols = df.select_dtypes(
            include="object"
        ).columns

        for col in cat_cols:
            df[col] = df[col].fillna(
                df[col].mode()[0]
            )

        return df

    # ==========================================
    # Duplicate Records
    # ==========================================

    @staticmethod
    def remove_duplicates(df):

        return df.drop_duplicates()

    # ==========================================
    # Date Conversion
    # ==========================================

    @staticmethod
    def convert_to_datetime(
            df,
            date_columns
    ):

        for col in date_columns:

            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            )

        return df

    # ==========================================
    # Feature Extraction
    # ==========================================

    @staticmethod
    def create_date_features(
            df,
            date_column
    ):

        df["year"] = df[date_column].dt.year
        df["quarter"] = df[date_column].dt.quarter
        df["month"] = df[date_column].dt.month
        df["week"] = df[date_column].dt.isocalendar().week
        df["day"] = df[date_column].dt.day

        return df

    # ==========================================
    # Outlier Handling
    # ==========================================

    @staticmethod
    def cap_outliers_iqr(df, column):

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - (1.5 * iqr)
        upper = q3 + (1.5 * iqr)

        df[column] = np.where(
            df[column] < lower,
            lower,
            df[column]
        )

        df[column] = np.where(
            df[column] > upper,
            upper,
            df[column]
        )

        return df

    # ==========================================
    # Label Encoding
    # ==========================================

    @staticmethod
    def label_encode(df):

        encoders = {}

        cat_cols = df.select_dtypes(
            include="object"
        ).columns

        for col in cat_cols:

            encoder = LabelEncoder()

            df[col] = encoder.fit_transform(
                df[col].astype(str)
            )

            encoders[col] = encoder

        return df, encoders

    # ==========================================
    # Standard Scaling
    # ==========================================

    @staticmethod
    def standard_scale(df, columns):

        scaler = StandardScaler()

        df[columns] = scaler.fit_transform(
            df[columns]
        )

        return df, scaler

    # ==========================================
    # MinMax Scaling
    # ==========================================

    @staticmethod
    def minmax_scale(df, columns):

        scaler = MinMaxScaler()

        df[columns] = scaler.fit_transform(
            df[columns]
        )

        return df, scaler
    

#Revenue Feature Engineering
import numpy as np
import pandas as pd


class RevenueFeatureEngineering:

    # ==========================================
    # Collection Rate
    # ==========================================

    @staticmethod
    def collection_rate(df):

        df["collection_rate"] = np.where(
            df["gross_revenue"] > 0,
            (
                df["payments_collected"]
                /
                df["gross_revenue"]
            ) * 100,
            0
        )

        return df

    # ==========================================
    # Reimbursement Rate
    # ==========================================

    @staticmethod
    def reimbursement_rate(df):

        df["reimbursement_rate"] = np.where(
            df["expected_reimbursement"] > 0,
            (
                df["payments_collected"]
                /
                df["expected_reimbursement"]
            ) * 100,
            0
        )

        return df

    # ==========================================
    # Denial Rate
    # ==========================================

    @staticmethod
    def denial_rate(df):

        df["denial_rate"] = np.where(
            df["claims_submitted"] > 0,
            (
                df["claims_denied"]
                /
                df["claims_submitted"]
            ) * 100,
            0
        )

        return df

    # ==========================================
    # Approval Rate
    # ==========================================

    @staticmethod
    def approval_rate(df):

        df["approval_rate"] = np.where(
            df["claims_submitted"] > 0,
            (
                df["claims_approved"]
                /
                df["claims_submitted"]
            ) * 100,
            0
        )

        return df

    # ==========================================
    # Revenue Leakage
    # ==========================================

    @staticmethod
    def revenue_leakage(df):

        df["revenue_leakage"] = (
            df["expected_reimbursement"]
            -
            df["payments_collected"]
        )

        return df

    # ==========================================
    # Net Revenue
    # ==========================================

    @staticmethod
    def net_revenue(df):

        if "write_offs" not in df.columns:
            df["write_offs"] = 0

        if "adjustments" not in df.columns:
            df["adjustments"] = 0

        df["net_revenue"] = (

            df["gross_revenue"]

            - df["write_offs"]

            - df["adjustments"]

        )

        return df

    # ==========================================
    # Collection Gap
    # ==========================================

    @staticmethod
    def collection_gap(df):

        df["collection_gap"] = (

            df["gross_revenue"]

            - df["payments_collected"]

        )

        return df

    # ==========================================
    # Reimbursement Gap
    # ==========================================

    @staticmethod
    def reimbursement_gap(df):

        df["reimbursement_gap"] = (

            df["expected_reimbursement"]

            - df["payments_collected"]

        )

        return df

    # ==========================================
    # Average Revenue Per Claim
    # ==========================================

    @staticmethod
    def revenue_per_claim(df):

        df["revenue_per_claim"] = np.where(
            df["claims_submitted"] > 0,
            (
                df["gross_revenue"]
                /
                df["claims_submitted"]
            ),
            0
        )

        return df

    # ==========================================
    # Revenue Efficiency
    # ==========================================

    @staticmethod
    def revenue_efficiency(df):

        df["revenue_efficiency"] = np.where(
            df["gross_revenue"] > 0,
            (
                df["payments_collected"]
                /
                df["gross_revenue"]
            ) * 100,
            0
        )

        return df

    # ==========================================
    # AR Days
    # ==========================================

    @staticmethod
    def ar_days(df):

        if "ar_balance" not in df.columns:
            return df

        daily_revenue = (
            df["gross_revenue"] / 30
        )

        df["ar_days"] = np.where(
            daily_revenue > 0,
            (
                df["ar_balance"]
                /
                daily_revenue
            ),
            0
        )

        return df

    # ==========================================
    # Revenue Risk Score
    # ==========================================

    @staticmethod
    def revenue_risk_score(df):

        denial_score = (
            df["claims_denied"]
            /
            df["claims_submitted"]
        )

        leakage_score = (
            (
                df["expected_reimbursement"]
                -
                df["payments_collected"]
            )
            /
            df["expected_reimbursement"]
        )

        df["revenue_risk_score"] = (
            (
                denial_score.fillna(0)
                +
                leakage_score.fillna(0)
            )
            * 50
        )

        return df

    # ==========================================
    # Revenue Growth
    # ==========================================

    @staticmethod
    def revenue_growth(df):

        df = df.sort_values(
            "service_date"
        )

        df["revenue_growth_pct"] = (

            df["gross_revenue"]
            .pct_change()

            * 100

        )

        return df

    # ==========================================
    # Forecasting Features
    # ==========================================

    @staticmethod
    def forecasting_features(df):

        df["service_date"] = pd.to_datetime(
            df["service_date"]
        )

        df["year"] = (
            df["service_date"]
            .dt.year
        )

        df["quarter"] = (
            df["service_date"]
            .dt.quarter
        )

        df["month"] = (
            df["service_date"]
            .dt.month
        )

        df["week"] = (
            df["service_date"]
            .dt.isocalendar()
            .week
        )

        df["day"] = (
            df["service_date"]
            .dt.day
        )

        return df