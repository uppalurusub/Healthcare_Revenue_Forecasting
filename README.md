# 🏥 Healthcare Revenue Forecasting System

> A Full-Stack Healthcare Revenue Cycle Management (RCM) Analytics and Revenue Forecasting Platform built using **FastAPI**, **React.js**, **TypeScript**, and **Machine Learning**.

---

# 📌 Project Overview

Healthcare organizations generate enormous amounts of financial data through patient billing, insurance claims, collections, denials, and reimbursements.

This project provides a complete analytics platform for monitoring the healthcare revenue cycle while forecasting future revenue using statistical forecasting models.

The solution consists of:

- FastAPI Backend REST APIs
- React.js Frontend Dashboard
- Healthcare Financial Analytics
- Revenue Forecasting
- Dynamic KPI Dashboards
- Interactive Charts
- REST API Integration

---

# System Architecture

```
                    +----------------------+
                    |    React Frontend    |
                    |  React + TypeScript  |
                    +----------+-----------+
                               |
                     REST APIs (Axios)
                               |
                +--------------v--------------+
                |        FastAPI Backend      |
                | Routers → Services → Logic  |
                +--------------+--------------+
                               |
                Analytics / Forecasting Engine
                               |
        +----------+-----------+------------+
        |          |           |            |
     Revenue    Claims     Payments     Denials
        |          |           |            |
        +----------+-----------+------------+
                               |
                     CSV Healthcare Dataset
```

---

# Project Structure

```
Healthcare_Revenue_Forecasting
│
├── backend
│   ├── data
│   ├── healthcare-revenue-forecasting-python-app
│   │
│   ├── implementations
│   ├── routers
│   ├── services
│   ├── utils
│   ├── visualizations
│   ├── models
│   └── main.py
│
├── ui
│   └── reactjs
│       └── healthcare-revenue-forecasting-react-app
│           ├── src
│           │   ├── api
│           │   ├── components
│           │   ├── config
│           │   ├── pages
│           │   ├── types
│           │   └── utils
│           └── package.json
│
├── requirements.txt
└── README.md
```

---

# Features

## Executive Dashboard

- Revenue KPIs
- Collections
- Claims Summary
- Denials Summary
- AR Aging Summary
- Payment Summary
- Forecast Overview

---

## Revenue Analytics

- Total Revenue
- Revenue Trend
- Monthly Revenue
- Department Revenue
- Insurance Revenue
- Revenue Distribution
- Top Departments
- Revenue Correlation

---

## Claims Analytics

- Total Claims
- Approved Claims
- Pending Claims
- Rejected Claims
- Claim Status Distribution
- Claim Amount Analysis
- Processing Metrics

---

## Payments Analytics

- Payment Trends
- Collection Rate
- Outstanding Amount
- Payment Methods
- Payment Distribution
- Payment KPIs

---

## Denials Analytics

- Denial Rate
- Denial Reasons
- Department-wise Denials
- Insurance-wise Denials
- Financial Impact
- Trend Analysis

---

## Accounts Receivable (AR Aging)

- Current
- 30 Days
- 60 Days
- 90 Days
- 120+ Days
- Outstanding Balance
- Aging Distribution

---

## Patient Billing

- Total Bills
- Paid Bills
- Pending Bills
- Outstanding Balance
- Billing Trends
- Collection Efficiency

---

## Revenue Forecasting

- Prophet Forecasting
- Future Revenue Prediction
- Trend Detection
- Seasonality Analysis
- Confidence Interval
- Forecast Charts

---

# Technology Stack

## Backend

- Python
- FastAPI
- Pandas
- NumPy
- Prophet
- Matplotlib
- Plotly
- Scikit-Learn
- Uvicorn

---

## Frontend

- React 19
- TypeScript
- Vite
- Axios
- React Router
- Recharts

---

## Visualization

- KPI Cards
- Dynamic Tables
- Line Charts
- Bar Charts
- Pie Charts
- Forecast Graphs

---

# Backend Architecture

```
Router
   │
   ▼
Service
   │
   ▼
Implementation
   │
   ▼
Utilities
   │
   ▼
Dataset
```

---

# Backend Modules

```
routers/

dashboard_router.py
revenue_router.py
claims_router.py
payments_router.py
denials_router.py
ar_aging_router.py
patient_billing_router.py
forecasting_router.py
```

---

# Service Layer

```
services/

dashboard_service.py
revenue_service.py
claims_service.py
payments_service.py
denials_service.py
ar_aging_service.py
patient_billing_service.py
forecasting_service.py
```

---

# Implementation Layer

```
implementations/

dashboard_impl.py
revenue_impl.py
claims_impl.py
payments_impl.py
denials_impl.py
ar_aging_impl.py
patient_billing_impl.py
forecasting_impl.py
prophet_model_impl.py
```

---

# Frontend Architecture

```
React
   │
   ▼
Pages
   │
   ▼
Components
   │
   ▼
Axios API
   │
   ▼
FastAPI
```

---

# Frontend Components

```
src/

api/
components/
config/
pages/
types/
utils/

App.tsx
main.tsx
```

---

# Dataset

The application includes healthcare financial datasets.

- revenue.csv
- claims.csv
- payments.csv
- denials.csv
- patient_billing.csv
- ar_aging.csv

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Healthcare_Revenue_Forecasting.git

cd Healthcare_Revenue_Forecasting
```

---

# Backend Setup

## Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Backend

```bash
cd backend/healthcare-revenue-forecasting-python-app

uvicorn main:app --reload
```

Backend URL

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# Frontend Setup

```bash
cd ui/reactjs/healthcare-revenue-forecasting-react-app
```

Install packages

```bash
npm install
```

Start application

```bash
npm run dev
```

Application

```
http://localhost:5173
```

---

# API Modules

| Module | Description |
|---------|-------------|
| Dashboard | Executive KPIs |
| Revenue | Revenue Analytics |
| Claims | Claims Analytics |
| Payments | Payment Analytics |
| Denials | Denial Analytics |
| AR Aging | Outstanding Receivables |
| Patient Billing | Billing Analytics |
| Forecasting | Revenue Forecasting |

---

# Forecasting Workflow

```
Historical Revenue
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Prophet Model
        │
        ▼
Revenue Prediction
        │
        ▼
Forecast Visualization
```

---

# Key Features

- Layered Architecture
- REST APIs
- Dynamic React Dashboard
- Modular Design
- KPI Analytics
- Forecasting Engine
- Interactive Charts
- Reusable Components
- TypeScript Frontend
- FastAPI Backend
- Clean Code Structure

---

# Future Enhancements

- Authentication & Authorization
- PostgreSQL Integration
- Docker Support
- Kubernetes Deployment
- CI/CD Pipeline
- MLflow Model Tracking
- XGBoost Revenue Prediction
- LSTM Forecasting
- AutoML Support
- Cloud Deployment (Azure/AWS)

---

# Contributors

Developed as a Healthcare Revenue Cycle Management Analytics and Forecasting platform demonstrating modern full-stack development, healthcare analytics, and machine learning best practices.

---

# License

This project is intended for educational, research, and demonstration purposes. Customize the license before production use.