import pandas as pd
from pathlib import Path


class DataLoader:

    DATASET_DIR = Path("../data")

    

    @staticmethod
    def load_csv(file_name: str) -> pd.DataFrame:
        """
        Generic CSV Loader
        """

        file_path = DataLoader.DATASET_DIR / file_name

        if not file_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {file_path}"
            )

        return pd.read_csv(file_path)

    # =====================================================
    # Revenue
    # =====================================================

    @staticmethod
    def load_revenue():
        return DataLoader.load_csv(
            "revenue.csv"
        )

    # =====================================================
    # Claims
    # =====================================================

    @staticmethod
    def load_claims():
        return DataLoader.load_csv(
            "claims.csv"
        )

    # =====================================================
    # Payments
    # =====================================================

    @staticmethod
    def load_payments():
        return DataLoader.load_csv(
            "payments.csv"
        )

    # =====================================================
    # Denials
    # =====================================================

    @staticmethod
    def load_denials():
        return DataLoader.load_csv(
            "denials.csv"
        )

    # =====================================================
    # AR Aging
    # =====================================================

    @staticmethod
    def load_ar_aging():
        return DataLoader.load_csv(
            "ar_aging.csv"
        )

    # =====================================================
    # Patient Billing
    # =====================================================

    @staticmethod
    def load_patient_billing():
        return DataLoader.load_csv(
            "patient_billing.csv"
        )

    # =====================================================
    # Load Everything
    # =====================================================

    @staticmethod
    def load_all():

        return {
            "revenue":
                DataLoader.load_revenue(),

            "claims":
                DataLoader.load_claims(),

            "payments":
                DataLoader.load_payments(),

            "denials":
                DataLoader.load_denials(),

            "ar_aging":
                DataLoader.load_ar_aging(),

            "patient_billing":
                DataLoader.load_patient_billing()
        }