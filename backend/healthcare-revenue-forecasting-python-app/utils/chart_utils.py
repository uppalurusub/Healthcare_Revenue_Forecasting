import os
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

OUTPUT_DIR = BASE_DIR / "outputs"

#OUTPUT_DIR = "outputs"



REVENUE_DIR = OUTPUT_DIR / "revenue"

PAYMENTS_DIR = OUTPUT_DIR / "payments"

PATIENTS_BILLING_DIR = OUTPUT_DIR / "patients_billing"

FORECASTING_DIR = OUTPUT_DIR / "forecasting"

DENIALS_DIR = OUTPUT_DIR / "denials"

DASHBOARD_DIR = OUTPUT_DIR / "dashboard"

CLAIMS_DIR = OUTPUT_DIR / "clains"

AR_AGING_DIR = OUTPUT_DIR / "ar_aging"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

os.makedirs(
    REVENUE_DIR,
    exist_ok=True
)

os.makedirs(
    PAYMENTS_DIR,
    exist_ok=True
)

os.makedirs(
    PATIENTS_BILLING_DIR,
    exist_ok=True
)

os.makedirs(
    FORECASTING_DIR,
    exist_ok=True
)

os.makedirs(
    DENIALS_DIR,
    exist_ok=True
)

os.makedirs(
    DASHBOARD_DIR,
    exist_ok=True
)

os.makedirs(
    CLAIMS_DIR,
    exist_ok=True
)

os.makedirs(
    AR_AGING_DIR,
    exist_ok=True
)


def save_chart_revenue_collection_trend(filename):

    filepath = f"{REVENUE_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath


def save_chart_revenue_leakage(filename):

    filepath = f"{REVENUE_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath


def save_chart_revenue_distribution(filename):

    filepath = f"{REVENUE_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath



def save_chart_revenue_box(filename):

    filepath = f"{REVENUE_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath


def save_chart_revenue_collection(filename):

    filepath = f"{REVENUE_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_revenue_correlation(filename):

    filepath = f"{REVENUE_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_revenue_top_payer(filename):

    filepath = f"{REVENUE_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_revenue_top_department(filename):

    filepath = f"{REVENUE_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_revenue_payer(filename):

    filepath = f"{REVENUE_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_revenue_monthly(filename):

    filepath = f"{REVENUE_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath


def save_chart_revenue_department(filename):

    filepath = f"{REVENUE_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

"""
def save_chart_predictions(filename):

    filepath = f"{PREDICTION_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_financial(filename):

    filepath = f"{FINANCIAL_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_outcomes(filename):

    filepath = f"{OUTCOMES_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_clinical_risk(filename):

    filepath = f"{CLINICAL_RISK_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_population_health(filename):

    filepath = f"{POPULATION_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_clinical(filename):

    filepath = f"{CLINICAL_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath
"""