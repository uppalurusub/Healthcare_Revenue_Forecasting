import type { EndpointDefinition } from '../types/api';

export const ENDPOINTS: Record<string, EndpointDefinition[]> = {
  "ar-aging": [
    {
      "path": "/summary",
      "label": "Ar Summary"
    },
    {
      "path": "/trend",
      "label": "Ar Trend"
    },
    {
      "path": "/monthly",
      "label": "Monthly Ar"
    },
    {
      "path": "/aging-buckets",
      "label": "Aging Buckets"
    },
    {
      "path": "/collection-status",
      "label": "Collection Status"
    },
    {
      "path": "/risk-analysis",
      "label": "Risk Analysis"
    },
    {
      "path": "/payer",
      "label": "Payer Analysis"
    },
    {
      "path": "/department",
      "label": "Department Analysis"
    },
    {
      "path": "/expected-collections",
      "label": "Expected Collections"
    },
    {
      "path": "/high-risk",
      "label": "High Risk Accounts"
    },
    {
      "path": "/top-payers",
      "label": "Top Payers",
      "params": {
        "top_n": 10
      }
    },
    {
      "path": "/kpis",
      "label": "Ar Kpis"
    }
  ],
  "claims": [
    {
      "path": "/summary",
      "label": "Claims Summary"
    },
    {
      "path": "/trend",
      "label": "Claims Trend"
    },
    {
      "path": "/monthly",
      "label": "Monthly Claims"
    },
    {
      "path": "/status",
      "label": "Claim Status"
    },
    {
      "path": "/denials",
      "label": "Denial Analysis"
    },
    {
      "path": "/denial-reasons",
      "label": "Denial Reasons"
    },
    {
      "path": "/payer",
      "label": "Payer Analysis"
    },
    {
      "path": "/department",
      "label": "Department Analysis"
    },
    {
      "path": "/reimbursement",
      "label": "Reimbursement Analysis"
    },
    {
      "path": "/top-denial-reasons",
      "label": "Top Denial Reasons",
      "params": {
        "top_n": 10
      }
    },
    {
      "path": "/kpis",
      "label": "Claims Kpis"
    }
  ],
  "dashboard": [
    {
      "path": "/",
      "label": "Executive Dashboard"
    },
    {
      "path": "/summary",
      "label": "Executive Summary"
    },
    {
      "path": "/revenue",
      "label": "Revenue Dashboard"
    },
    {
      "path": "/claims",
      "label": "Claims Dashboard"
    },
    {
      "path": "/payments",
      "label": "Payments Dashboard"
    },
    {
      "path": "/denials",
      "label": "Denials Dashboard"
    },
    {
      "path": "/ar-aging",
      "label": "Ar Dashboard"
    },
    {
      "path": "/patient-billing",
      "label": "Patient Billing Dashboard"
    },
    {
      "path": "/forecast",
      "label": "Forecast Dashboard"
    },
    {
      "path": "/kpis",
      "label": "Dashboard Kpis"
    }
  ],
  "denials": [
    {
      "path": "/summary",
      "label": "Denial Summary"
    },
    {
      "path": "/trend",
      "label": "Denial Trend"
    },
    {
      "path": "/monthly",
      "label": "Monthly Denials"
    },
    {
      "path": "/reasons",
      "label": "Denial Reasons"
    },
    {
      "path": "/categories",
      "label": "Denial Categories"
    },
    {
      "path": "/department",
      "label": "Department Analysis"
    },
    {
      "path": "/payer",
      "label": "Payer Analysis"
    },
    {
      "path": "/appeals",
      "label": "Appeal Analysis"
    },
    {
      "path": "/recovery",
      "label": "Recovery Analysis"
    },
    {
      "path": "/resolution",
      "label": "Resolution Analysis"
    },
    {
      "path": "/top-reasons",
      "label": "Top Denial Reasons",
      "params": {
        "top_n": 10
      }
    },
    {
      "path": "/revenue-leakage",
      "label": "Revenue Leakage"
    },
    {
      "path": "/kpis",
      "label": "Denial Kpis"
    }
  ],
  "forecasting": [
    {
      "path": "/revenue",
      "label": "Revenue Forecast",
      "params": {
        "periods": 12
      }
    },
    {
      "path": "/collections",
      "label": "Collection Forecast",
      "params": {
        "periods": 12
      }
    },
    {
      "path": "/ar",
      "label": "Ar Forecast",
      "params": {
        "periods": 12
      }
    },
    {
      "path": "/growth",
      "label": "Revenue Growth Forecast",
      "params": {
        "periods": 12
      }
    },
    {
      "path": "/scenario",
      "label": "Scenario Forecast",
      "params": {
        "periods": 12
      }
    },
    {
      "path": "/model-comparison",
      "label": "Model Comparison"
    },
    {
      "path": "/evaluation",
      "label": "Forecast Evaluation"
    },
    {
      "path": "/summary",
      "label": "Forecast Summary"
    },
    {
      "path": "/kpis",
      "label": "Forecast Kpis"
    }
  ],
  "patient-billing": [
    {
      "path": "/summary",
      "label": "Billing Summary"
    },
    {
      "path": "/trend",
      "label": "Billing Trend"
    },
    {
      "path": "/monthly",
      "label": "Monthly Billing"
    },
    {
      "path": "/status",
      "label": "Billing Status"
    },
    {
      "path": "/payment-plans",
      "label": "Payment Plan Analysis"
    },
    {
      "path": "/department",
      "label": "Department Analysis"
    },
    {
      "path": "/payer",
      "label": "Payer Analysis"
    },
    {
      "path": "/outstanding-balances",
      "label": "Outstanding Balances"
    },
    {
      "path": "/collections",
      "label": "Collection Analysis"
    },
    {
      "path": "/payment-plan-performance",
      "label": "Payment Plan Performance"
    },
    {
      "path": "/top-patients",
      "label": "Top Outstanding Patients",
      "params": {
        "top_n": 20
      }
    },
    {
      "path": "/kpis",
      "label": "Billing Kpis"
    }
  ],
  "payments": [
    {
      "path": "/summary",
      "label": "Payment Summary"
    },
    {
      "path": "/trend",
      "label": "Payment Trend"
    },
    {
      "path": "/monthly",
      "label": "Monthly Payments"
    },
    {
      "path": "/status",
      "label": "Payment Status"
    },
    {
      "path": "/insurance",
      "label": "Insurance Payments"
    },
    {
      "path": "/patient",
      "label": "Patient Payments"
    },
    {
      "path": "/payer",
      "label": "Payer Analysis"
    },
    {
      "path": "/payment-method",
      "label": "Payment Method Analysis"
    },
    {
      "path": "/collections",
      "label": "Collection Analysis"
    },
    {
      "path": "/days-to-payment",
      "label": "Days To Payment"
    },
    {
      "path": "/top-payers",
      "label": "Top Payers",
      "params": {
        "top_n": 10
      }
    },
    {
      "path": "/kpis",
      "label": "Payment Kpis"
    }
  ],
  "revenue": [
    {
      "path": "/summary",
      "label": "Revenue Summary"
    },
    {
      "path": "/trend",
      "label": "Revenue Trend"
    },
    {
      "path": "/monthly",
      "label": "Monthly Revenue"
    },
    {
      "path": "/department",
      "label": "Revenue By Department"
    },
    {
      "path": "/payer",
      "label": "Revenue By Payer"
    },
    {
      "path": "/collections",
      "label": "Collection Analysis"
    },
    {
      "path": "/leakage",
      "label": "Revenue Leakage"
    },
    {
      "path": "/top-departments",
      "label": "Top Departments",
      "params": {
        "top_n": 10
      }
    },
    {
      "path": "/top-payers",
      "label": "Top Payers",
      "params": {
        "top_n": 10
      }
    },
    {
      "path": "/kpis",
      "label": "Revenue Kpis"
    },
    {
      "path": "/monthly/chart",
      "label": "Monthly Chart"
    },
    {
      "path": "/department/chart",
      "label": "Department Chart"
    },
    {
      "path": "/payer/chart",
      "label": "Payer Chart"
    },
    {
      "path": "/top-departments/chart",
      "label": "Top Departments",
      "params": {
        "top_n": 10
      }
    },
    {
      "path": "/top-payers/chart",
      "label": "Top Payers",
      "params": {
        "top_n": 10
      }
    },
    {
      "path": "/distribution/chart",
      "label": "Revenue Distribution Chart"
    },
    {
      "path": "/outliers/chart",
      "label": "Revenue Boxplot Chart"
    },
    {
      "path": "/collection-revenue/chart",
      "label": "Revenue Vs Collections Chart"
    },
    {
      "path": "/correlation/chart",
      "label": "Correlation Heatmap Chart"
    }
  ]
};
