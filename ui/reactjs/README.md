# Healthcare Revenue Cycle Management Analytics Dashboard

A modern **React.js + TypeScript analytics dashboard** for visualizing Healthcare Revenue Cycle Management (RCM) data.

The application integrates with a REST API backend and provides interactive dashboards for:

* Accounts Receivable Aging
* Claims Analytics
* Executive Dashboard
* Denial Analytics
* Revenue Forecasting
* Patient Billing
* Payments
* Revenue Analytics

The UI dynamically renders API responses as KPI cards, nested analytics sections, tabular datasets, interactive charts, and backend-generated chart images.

---

## Overview

Healthcare Revenue Cycle Management involves tracking financial processes across the patient care lifecycle, including claims, payments, denials, outstanding balances, collections, and revenue forecasting.

This React application provides a centralized analytics interface for consuming RCM analytics APIs.

The frontend uses a **configuration-driven architecture**. Analytics modules and API endpoints are defined centrally and rendered dynamically using reusable React components.

The application automatically:

1. Identifies the selected analytics module.
2. Loads configured endpoints for the module.
3. Calls the appropriate REST API.
4. Detects JSON or image responses.
5. Dynamically renders KPI cards, nested sections, or tables.
6. Detects chart-compatible datasets.
7. Selects an appropriate visualization.
8. Displays the analytics results.

---

## Key Features

### Healthcare RCM Analytics

The application provides analytics capabilities across major Revenue Cycle Management domains.

Supported modules include:

| Module          | Description                                                             |
| --------------- | ----------------------------------------------------------------------- |
| AR Aging        | Accounts receivable aging, collection status, risk, and payer analytics |
| Claims          | Claims trends, status, denials, reimbursement, and payer analytics      |
| Dashboard       | Executive-level RCM dashboards and KPI summaries                        |
| Denials         | Denial trends, reasons, categories, appeals, recovery, and leakage      |
| Forecasting     | Revenue, collections, AR, growth, and scenario forecasting              |
| Patient Billing | Patient balances, payment plans, billing trends, and collections        |
| Payments        | Insurance payments, patient payments, payment methods, and collections  |
| Revenue         | Revenue trends, departments, payers, collections, and leakage           |

---

## Dynamic API Integration

The application dynamically builds API requests using the selected module and endpoint.

Example:

```text
http://127.0.0.1:8000/api/{module}/{endpoint}
```

Examples:

```text
http://127.0.0.1:8000/api/dashboard
http://127.0.0.1:8000/api/dashboard/summary
http://127.0.0.1:8000/api/revenue/summary
http://127.0.0.1:8000/api/claims/trend
http://127.0.0.1:8000/api/denials/reasons
http://127.0.0.1:8000/api/patient-billing/summary
http://127.0.0.1:8000/api/forecasting/revenue
```

Query parameters are configured directly in the endpoint registry.

Example:

```typescript
{
  path: '/top-payers',
  label: 'Top Payers',
  params: {
    top_n: 10
  }
}
```

The resulting request is equivalent to:

```text
GET /api/revenue/top-payers?top_n=10
```

---

## Technology Stack

| Technology   | Purpose                                |
| ------------ | -------------------------------------- |
| React        | Component-based user interface         |
| TypeScript   | Static typing and maintainability      |
| React Router | Client-side module routing             |
| Axios        | REST API communication                 |
| Recharts     | Interactive analytics visualizations   |
| Vite         | Frontend development and build tooling |
| CSS          | Responsive dashboard styling           |

---

## Application Architecture

The application follows a modular and configuration-driven architecture.

```text
src/
│
├── api/
│   ├── analyticsApi.ts
│   └── httpClient.ts
│
├── components/
│   ├── charts/
│   │   └── AnalyticsChart.tsx
│   │
│   ├── DataRenderer.tsx
│   └── Sidebar.tsx
│
├── config/
│   ├── api.ts
│   └── endpoints.ts
│
├── pages/
│   └── ModulePage.tsx
│
├── types/
│   └── api.ts
│
├── utils/
│   ├── chartAdapter.ts
│   └── formatters.ts
│
├── App.tsx
├── main.tsx
└── styles.css
```

---

## Architecture Flow

```text
User
 │
 ▼
Sidebar
 │
 ▼
React Router
 │
 ▼
ModulePage
 │
 ▼
ENDPOINTS Configuration
 │
 ▼
getAnalytics()
 │
 ▼
Axios HTTP Client
 │
 ▼
Healthcare RCM REST API
 │
 ├──────────── JSON Response
 │                   │
 │                   ▼
 │             DataRenderer
 │                   │
 │                   ▼
 │             chartAdapter
 │                   │
 │                   ▼
 │             AnalyticsChart
 │
 └──────────── Image Response
                     │
                     ▼
                API Chart
```

---

## Project Components

### `App.tsx`

The main application component configures routing and the global application layout.

```typescript
export default function App() {
  return (
    <div className="app-shell">
      <Sidebar />

      <Routes>
        <Route path="/:module" element={<ModulePage />} />
        <Route
          path="*"
          element={<Navigate to="/dashboard" replace />}
        />
      </Routes>
    </div>
  );
}
```

The application uses dynamic routes.

Examples:

```text
/dashboard
/revenue
/claims
/denials
/ar-aging
/forecasting
/patient-billing
/payments
```

Unknown routes automatically redirect to:

```text
/dashboard
```

---

## API Layer

### `api/httpClient.ts`

A centralized Axios client is used for all API communication.

```typescript
import axios from 'axios';
import { API_BASE_URL } from '../config/api';

export const httpClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000,
  headers: {
    Accept: 'application/json, image/png'
  }
});
```

Benefits of a centralized HTTP client include:

* Centralized API base URL
* Common timeout configuration
* Shared HTTP headers
* Simplified API services
* Easier interceptor integration
* Centralized authentication support

---

### `api/analyticsApi.ts`

The analytics service dynamically calls analytics endpoints.

```typescript
export async function getAnalytics(
  module: string,
  path: string,
  params?: Record<string, number>
): Promise<AnalyticsResponse> {
  const url = `/${module}${path === '/' ? '' : path}`;

  if (path.endsWith('/chart')) {
    const response = await httpClient.get<Blob>(url, {
      params,
      responseType: 'blob'
    });

    return {
      kind: 'image',
      data: URL.createObjectURL(response.data)
    };
  }

  const response = await httpClient.get<ApiValue>(url, {
    params
  });

  return {
    kind: 'json',
    data: response.data
  };
}
```

The service supports two API response types.

### JSON Responses

JSON analytics responses are returned as:

```typescript
{
  kind: 'json',
  data: response.data
}
```

### Image Responses

Endpoints ending with `/chart` are treated as image endpoints.

```typescript
{
  kind: 'image',
  data: URL.createObjectURL(response.data)
}
```

This allows backend-generated visualizations such as:

* Heatmaps
* Box plots
* Distribution charts
* Correlation charts
* Custom analytical plots

---

## API Configuration

### `config/api.ts`

The API base URL is environment configurable.

```typescript
export const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL ??
  'http://127.0.0.1:8000/api';
```

The application first checks:

```text
VITE_API_BASE_URL
```

If the environment variable is unavailable, the default API URL is:

```text
http://127.0.0.1:8000/api
```

---

## Endpoint Registry

### `config/endpoints.ts`

All analytics modules and API endpoints are centrally configured using the `ENDPOINTS` registry.

```typescript
export const ENDPOINTS: Record<
  string,
  EndpointDefinition[]
> = {
  revenue: [
    {
      path: '/summary',
      label: 'Revenue Summary'
    },
    {
      path: '/trend',
      label: 'Revenue Trend'
    }
  ]
};
```

This architecture removes endpoint-specific UI implementation from React pages.

To add a new endpoint, update the configuration.

Example:

```typescript
{
  path: '/yearly',
  label: 'Yearly Revenue'
}
```

The application automatically:

* Creates a tab
* Calls the API
* Renders the response
* Attempts to create a chart

---

## Supported Analytics Endpoints

### AR Aging

```text
/ar-aging/summary
/ar-aging/trend
/ar-aging/monthly
/ar-aging/aging-buckets
/ar-aging/collection-status
/ar-aging/risk-analysis
/ar-aging/payer
/ar-aging/department
/ar-aging/expected-collections
/ar-aging/high-risk
/ar-aging/top-payers
/ar-aging/kpis
```

### Claims

```text
/claims/summary
/claims/trend
/claims/monthly
/claims/status
/claims/denials
/claims/denial-reasons
/claims/payer
/claims/department
/claims/reimbursement
/claims/top-denial-reasons
/claims/kpis
```

### Dashboard

```text
/dashboard
/dashboard/summary
/dashboard/revenue
/dashboard/claims
/dashboard/payments
/dashboard/denials
/dashboard/ar-aging
/dashboard/patient-billing
/dashboard/forecast
/dashboard/kpis
```

### Denials

```text
/denials/summary
/denials/trend
/denials/monthly
/denials/reasons
/denials/categories
/denials/department
/denials/payer
/denials/appeals
/denials/recovery
/denials/resolution
/denials/top-reasons
/denials/revenue-leakage
/denials/kpis
```

### Forecasting

```text
/forecasting/revenue
/forecasting/collections
/forecasting/ar
/forecasting/growth
/forecasting/scenario
/forecasting/model-comparison
/forecasting/evaluation
/forecasting/summary
/forecasting/kpis
```

Forecast endpoints use a default forecast horizon:

```typescript
params: {
  periods: 12
}
```

### Patient Billing

```text
/patient-billing/summary
/patient-billing/trend
/patient-billing/monthly
/patient-billing/status
/patient-billing/payment-plans
/patient-billing/department
/patient-billing/payer
/patient-billing/outstanding-balances
/patient-billing/collections
/patient-billing/payment-plan-performance
/patient-billing/top-patients
/patient-billing/kpis
```

### Payments

```text
/payments/summary
/payments/trend
/payments/monthly
/payments/status
/payments/insurance
/payments/patient
/payments/payer
/payments/payment-method
/payments/collections
/payments/days-to-payment
/payments/top-payers
/payments/kpis
```

### Revenue

```text
/revenue/summary
/revenue/trend
/revenue/monthly
/revenue/department
/revenue/payer
/revenue/collections
/revenue/leakage
/revenue/top-departments
/revenue/top-payers
/revenue/kpis
```

Revenue chart APIs include:

```text
/revenue/monthly/chart
/revenue/department/chart
/revenue/payer/chart
/revenue/top-departments/chart
/revenue/top-payers/chart
/revenue/distribution/chart
/revenue/outliers/chart
/revenue/collection-revenue/chart
/revenue/correlation/chart
```

---

## Dynamic Data Rendering

### `components/DataRenderer.tsx`

`DataRenderer` recursively analyzes API response structures.

It supports:

* Primitive values
* Objects
* Nested objects
* Arrays
* Arrays of objects

### Object Responses

Objects are displayed using responsive metric cards.

Example API response:

```json
{
  "total_revenue": 12451697.35,
  "total_claims": 15230,
  "collection_rate": 92.4
}
```

The application renders:

```text
Total Revenue
12,451,697.35

Total Claims
15,230

Collection Rate
92.4
```

### Array Responses

Arrays of objects are automatically rendered as tables.

Example:

```json
[
  {
    "payer": "Medicare",
    "revenue": 4500000
  },
  {
    "payer": "Medicaid",
    "revenue": 2800000
  }
]
```

The table columns are dynamically identified from the response.

### Nested Responses

Nested objects are recursively rendered as analytical sections.

Example:

```json
{
  "revenue_summary": {
    "total_revenue": 12451697,
    "net_revenue": 10850000
  }
}
```

The application automatically creates a nested analytics card for `revenue_summary`.

---

## Data Visualization

### `components/charts/AnalyticsChart.tsx`

The application uses Recharts to dynamically select a visualization based on the API endpoint and response structure.

Supported chart types include:

* Pie Chart
* Line Chart
* Area Chart
* Bar Chart
* Horizontal Bar Chart

---

## Automatic Chart Selection

The chart type is determined using endpoint naming patterns.

### Pie Chart

Pie charts are selected for categorical distribution endpoints.

Patterns:

```text
status
categories
reasons
payment-method
aging-buckets
```

Example:

```text
/claims/status
/denials/categories
/denials/reasons
/payments/payment-method
/ar-aging/aging-buckets
```

Conditions:

```text
Single numeric metric
Maximum eight categories
```

---

### Line Chart

Line charts are selected for temporal and forecasting data.

Patterns:

```text
trend
monthly
forecast
growth
```

Examples:

```text
/revenue/trend
/revenue/monthly
/claims/trend
/forecasting/revenue
/forecasting/growth
```

---

### Area Chart

Area charts are selected for multi-metric collection and reimbursement analysis.

Patterns:

```text
collections
reimbursement
expected
```

Examples:

```text
/revenue/collections
/claims/reimbursement
/ar-aging/expected-collections
```

The dataset must contain multiple numeric metrics.

---

### Bar Chart

Bar charts are used as the default visualization.

For datasets containing fewer than eight rows:

```text
Vertical bar chart
```

For datasets containing eight or more rows:

```text
Horizontal bar chart
```

This improves readability for larger categorical datasets.

---

## Chart Data Adapter

### `utils/chartAdapter.ts`

The chart adapter converts API data into a chart-compatible structure.

```typescript
export function toChartModel(
  value: ApiValue
): ChartModel | null
```

The adapter:

1. Searches the response recursively.
2. Identifies arrays containing objects.
3. Extracts available data keys.
4. Detects numeric columns.
5. Selects up to four numeric metrics.
6. Identifies a string-based category column.
7. Creates a `ChartModel`.

Example output:

```typescript
{
  data: rows,
  categoryKey: 'month',
  numericKeys: [
    'revenue',
    'collections'
  ]
}
```

This architecture allows the visualization layer to work with multiple analytics APIs without endpoint-specific chart transformation logic.

---

## TypeScript Data Model

### `types/api.ts`

The application defines recursive API data types.

```typescript
export type Primitive =
  | string
  | number
  | boolean
  | null;
```

Recursive API value:

```typescript
export type ApiValue =
  | Primitive
  | ApiObject
  | ApiValue[];
```

Dynamic API object:

```typescript
export interface ApiObject {
  [key: string]: ApiValue;
}
```

Endpoint definition:

```typescript
export interface EndpointDefinition {
  path: string;
  label: string;
  params?: Record<string, number>;
}
```

Analytics API responses use a discriminated union.

```typescript
export type AnalyticsResponse =
  | {
      kind: 'json';
      data: ApiValue;
    }
  | {
      kind: 'image';
      data: string;
    };
```

Chart model:

```typescript
export interface ChartModel {
  data: Record<string, unknown>[];
  categoryKey: string;
  numericKeys: string[];
}
```

---

## Main Analytics Page

### `pages/ModulePage.tsx`

`ModulePage` is the primary analytics orchestration component.

Responsibilities include:

* Reading the module from the route
* Loading configured endpoints
* Managing the selected endpoint
* Calling analytics APIs
* Managing loading state
* Managing API errors
* Rendering JSON responses
* Rendering API-generated images
* Creating chart models
* Displaying interactive charts

The module is extracted using:

```typescript
const { module = 'dashboard' } = useParams();
```

Configured endpoints are retrieved using:

```typescript
const endpoints = ENDPOINTS[module] ?? [];
```

The selected API endpoint is:

```typescript
const endpoint = endpoints[selected];
```

Analytics data is loaded whenever the module or endpoint changes.

```typescript
useEffect(() => {
  if (!endpoint) return;

  getAnalytics(
    module,
    endpoint.path,
    endpoint.params
  );
}, [module, endpoint]);
```

---

## Sidebar Navigation

### `components/Sidebar.tsx`

The sidebar is dynamically generated from the endpoint configuration.

```typescript
Object.keys(ENDPOINTS).map(module => (
  <NavLink
    key={module}
    to={`/${module}`}
  >
    {titleize(module)}
  </NavLink>
))
```

Current modules automatically appear in the sidebar.

Adding a new module to `ENDPOINTS` automatically creates a new navigation item.

---

## Utility Functions

### `utils/formatters.ts`

The project provides reusable formatting utilities.

### `titleize`

Converts API field names into readable labels.

```text
total_revenue
```

becomes:

```text
Total Revenue
```

Similarly:

```text
patient-billing
```

becomes:

```text
Patient Billing
```

### `formatValue`

Formats numeric values using locale-aware number formatting.

```typescript
value.toLocaleString(undefined, {
  maximumFractionDigits: 2
});
```

Example:

```text
12451697.35
```

becomes:

```text
12,451,697.35
```

Null or undefined values are displayed as:

```text
—
```

### `isMoneyKey`

Identifies financial metrics using field names.

Supported patterns include:

```text
revenue
amount
balance
payment
collection
cost
charge
billing
ar
leakage
```

Financial values receive currency formatting in chart tooltips.

---

## Environment Configuration

Create a `.env` file in the React project root.

```env
VITE_API_BASE_URL=http://127.0.0.1:8000/api
```

For another environment:

```env
VITE_API_BASE_URL=https://api.example.com/api
```

Restart the Vite development server after modifying environment variables.

---

## Prerequisites

Install the following software before running the application:

```text
Node.js 18+
npm 9+
```

The Healthcare RCM REST API must also be running.

Default backend URL:

```text
http://127.0.0.1:8000
```

Default frontend API base URL:

```text
http://127.0.0.1:8000/api
```

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
```

Navigate to the project directory.

```bash
cd <project-directory>
```

Install dependencies.

```bash
npm install
```

If creating the dependency setup manually, the core runtime packages used by the source are:

```bash
npm install react react-dom react-router-dom axios recharts
```

Install the TypeScript and Vite development dependencies required by your project configuration.

Example:

```bash
npm install -D typescript vite @vitejs/plugin-react @types/react @types/react-dom
```

---

## Running the Application

Start the backend API.

Example:

```bash
uvicorn main:app --reload
```

The backend should be available at:

```text
http://127.0.0.1:8000
```

Start the React development server.

```bash
npm run dev
```

Open the application using the URL displayed by Vite.

The default Vite development URL is commonly:

```text
http://localhost:5173
```

---

## Build for Production

Create a production build.

```bash
npm run build
```

The optimized frontend assets are generated in:

```text
dist/
```

Preview the production build locally.

```bash
npm run preview
```

---

## API Response Requirements

### KPI Response

```json
{
  "total_revenue": 12451697.35,
  "total_claims": 15000,
  "collection_rate": 92.5,
  "denial_rate": 7.4
}
```

This response is rendered as metric cards.

---

### Chart-Compatible Response

```json
[
  {
    "month": "Jan",
    "revenue": 1200000,
    "collections": 1050000
  },
  {
    "month": "Feb",
    "revenue": 1350000,
    "collections": 1180000
  },
  {
    "month": "Mar",
    "revenue": 1420000,
    "collections": 1250000
  }
]
```

The chart adapter identifies:

```text
Category Key: month

Numeric Keys:
revenue
collections
```

A visualization is automatically generated.

---

### Nested Analytics Response

```json
{
  "executive_summary": {
    "total_revenue": 12451697.35,
    "total_claims": 15000
  },
  "collection_metrics": {
    "collection_rate": 92.5,
    "average_days_to_payment": 31
  }
}
```

Each nested object is displayed in a separate analytics section.

---

### Image Response

Chart endpoints should return an image response such as:

```text
Content-Type: image/png
```

Example endpoints:

```text
/revenue/correlation/chart
/revenue/outliers/chart
```

The React application loads the response as a Blob and creates a temporary browser object URL.

---

## Loading and Error Handling

The application maintains explicit loading and error states.

Loading state:

```text
Loading analytics…
```

API errors are displayed in a dedicated error panel.

```typescript
setError(
  e instanceof Error
    ? e.message
    : 'Unable to load analytics'
);
```

The application also prevents stale API responses from updating an unmounted or changed page using an `active` flag.

Generated image object URLs are revoked during cleanup.

```typescript
URL.revokeObjectURL(imageUrl);
```

This prevents browser memory leaks.

---

## Responsive Design

The application includes responsive dashboard styling.

Desktop layout:

```text
250px fixed sidebar
Dynamic analytics content area
Responsive metric grids
Scrollable analytics tabs
```

Mobile and tablet layout below `800px`:

```text
76px compact sidebar
RCM abbreviated branding
Single-column KPI layout
Reduced content padding
Compact navigation labels
```

The metric grid uses:

```css
grid-template-columns:
  repeat(auto-fit, minmax(200px, 1fr));
```

This allows KPI cards to automatically adapt to the available screen width.

---

## Adding a New Analytics Module

Add a new module to `config/endpoints.ts`.

Example:

```typescript
export const ENDPOINTS = {
  quality: [
    {
      path: '/summary',
      label: 'Quality Summary'
    },
    {
      path: '/trend',
      label: 'Quality Trend'
    },
    {
      path: '/kpis',
      label: 'Quality KPIs'
    }
  ]
};
```

The application automatically creates:

```text
/quality
```

The sidebar displays:

```text
Quality
```

The following API calls become available:

```text
/api/quality/summary
/api/quality/trend
/api/quality/kpis
```

No changes are required in:

```text
App.tsx
Sidebar.tsx
ModulePage.tsx
DataRenderer.tsx
```

---

## Adding a New Endpoint

Add the endpoint to an existing module.

Example:

```typescript
{
  path: '/yearly',
  label: 'Yearly Revenue'
}
```

The application automatically creates a new analytics tab and calls:

```text
GET /api/revenue/yearly
```

---

## Adding Query Parameters

Configure query parameters using `params`.

```typescript
{
  path: '/top-payers',
  label: 'Top Payers',
  params: {
    top_n: 20
  }
}
```

The generated request is:

```text
GET /api/revenue/top-payers?top_n=20
```

---

## Design Principles

The project follows several frontend architecture principles.

### Configuration-Driven UI

Analytics modules and endpoints are managed centrally.

### Separation of Concerns

API communication, data rendering, chart adaptation, visualization, routing, and formatting are implemented independently.

### Reusable Components

The same components support multiple healthcare analytics modules.

### Recursive Data Rendering

Unknown nested API structures can be rendered without writing endpoint-specific UI components.

### Adaptive Visualization

Charts are selected dynamically using endpoint semantics and response structure.

### Type Safety

Recursive TypeScript types model flexible API responses while maintaining compile-time type checking.

### Responsive Analytics UI

The layout adapts to desktop, tablet, and smaller browser widths.

---

## Current Project Strengths

The current architecture provides:

* Centralized endpoint configuration
* Dynamic sidebar generation
* Dynamic module routing
* Reusable Axios API client
* JSON and image API support
* Recursive API response rendering
* Automatic table generation
* Automatic chart data detection
* Adaptive chart selection
* Recharts-based visualizations
* Financial tooltip formatting
* Loading and error handling
* Object URL lifecycle management
* Responsive dashboard design
* Strong TypeScript API models

---

## Recommended Future Enhancements

Potential production enhancements include:

* Authentication and authorization
* JWT or OAuth integration
* Axios request and response interceptors
* Role-based dashboard access
* Date range filters
* Payer filters
* Department filters
* Global analytics filters
* Configurable forecast periods
* React Query or TanStack Query integration
* API response caching
* Retry policies
* Skeleton loading components
* Chart export
* CSV and Excel export
* PDF report generation
* Dark mode
* Theme configuration
* Drill-down analytics
* Chart-level filters
* Dashboard widgets
* Custom dashboard layouts
* Unit testing with Vitest
* React Testing Library integration
* End-to-end testing with Playwright
* Error boundaries
* Structured frontend logging
* Docker deployment
* Nginx hosting
* CI/CD pipelines
* Kubernetes deployment
* Azure or AWS cloud deployment

---

## Recommended Production Architecture

```text
Browser
   │
   ▼
React + TypeScript
   │
   ├── React Router
   ├── Analytics Components
   ├── Recharts
   └── Axios
          │
          ▼
      API Gateway
          │
          ▼
       FastAPI
          │
   ┌──────┼─────────┐
   │      │         │
   ▼      ▼         ▼
Revenue  Claims   Forecasting
Service  Service    Service
   │      │         │
   └──────┼─────────┘
          │
          ▼
 Analytics / ML Layer
          │
   ┌──────┼───────────┐
   ▼      ▼           ▼
Database  ML Models   Data Lake
```

---

## Security Considerations

For production deployments:

* Never store secrets directly in React source code.
* Use environment variables for public frontend configuration.
* Keep database credentials and private API keys in the backend.
* Use HTTPS.
* Configure backend CORS explicitly.
* Implement authentication.
* Implement role-based authorization.
* Validate API requests on the backend.
* Protect sensitive healthcare and financial data.
* Apply appropriate HIPAA-aligned safeguards when handling protected health information.
* Avoid exposing patient-identifiable data in frontend logs.
* Implement audit logging where required.
* Apply secure session and token management.

---

## Troubleshooting

### API Connection Error

Verify the backend is running.

```text
http://127.0.0.1:8000
```

Verify the configured API base URL.

```env
VITE_API_BASE_URL=http://127.0.0.1:8000/api
```

---

### CORS Error

Configure CORS in the backend.

Example FastAPI configuration:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Use environment-specific origin allowlists in production.

---

### Charts Are Not Displayed

The automatic chart adapter requires:

* An array of objects
* At least two rows
* At least one numeric field

Example:

```json
[
  {
    "month": "Jan",
    "revenue": 100000
  },
  {
    "month": "Feb",
    "revenue": 120000
  }
]
```

---

### Chart Image Is Not Displayed

Verify the endpoint path ends with:

```text
/chart
```

The backend should return an image-compatible response.

Example:

```text
Content-Type: image/png
```

---

### Empty Module Page

Verify the module exists in:

```text
src/config/endpoints.ts
```

Example:

```typescript
ENDPOINTS['revenue']
```

Also verify the corresponding backend API route exists.

---

## Conclusion

The Healthcare Revenue Cycle Management Analytics Dashboard provides a reusable and scalable React.js and TypeScript frontend architecture for healthcare financial analytics.

Its configuration-driven endpoint registry enables analytics modules to be added with minimal frontend development. Recursive data rendering allows flexible REST API responses to be displayed as KPI cards, nested sections, and tables, while the chart adapter automatically converts analytical datasets into interactive Recharts visualizations.

The architecture is suitable as a foundation for enterprise healthcare analytics solutions covering revenue, claims, denials, accounts receivable, payments, patient billing, collections, and financial forecasting.

---

## License

Add the appropriate license for your organization or repository.

Example:

```text
MIT License
```

or:

```text
Proprietary - Internal Healthcare Analytics Platform
```

---

## Author

**Subrahmanyam Uppaluru**

Healthcare Analytics | AI/ML | Data Science | Software Architecture | Revenue Cycle Management
