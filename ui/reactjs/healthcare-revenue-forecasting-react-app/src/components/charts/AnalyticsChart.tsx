import {
  Area, AreaChart, Bar, BarChart, CartesianGrid, Legend, Line, LineChart,
  Pie, PieChart, ResponsiveContainer, Tooltip, XAxis, YAxis, Cell
} from 'recharts';
import type { ChartModel } from '../../types/api';
import { isMoneyKey, titleize } from '../../utils/formatters';

const COLORS = ['#2563eb','#0f766e','#7c3aed','#ea580c','#0891b2','#be123c','#4f46e5','#65a30d'];

interface Props { model: ChartModel; endpointPath: string; title: string }

export function AnalyticsChart({ model, endpointPath, title }: Props) {
  const { data, categoryKey, numericKeys } = model;
  const key = numericKeys[0];
  const tick = (value: number) => Intl.NumberFormat('en', { notation: 'compact', maximumFractionDigits: 1 }).format(value);
  const tooltipFormatter = (value: number, name: string) => [isMoneyKey(name) ? `$${Number(value).toLocaleString()}` : Number(value).toLocaleString(), titleize(name)];

  if (/(status|categories|reasons|payment-method|aging-buckets)/i.test(endpointPath) && numericKeys.length === 1 && data.length <= 8) {
    return <div className="chart-card"><h3>{title}</h3><ResponsiveContainer width="100%" height={380}>
      <PieChart><Pie data={data} dataKey={key} nameKey={categoryKey} cx="50%" cy="50%" outerRadius={125} label>
        {data.map((_, i) => <Cell key={i} fill={COLORS[i % COLORS.length]} />)}
      </Pie><Tooltip formatter={tooltipFormatter} /><Legend /></PieChart>
    </ResponsiveContainer></div>;
  }

  if (/(trend|monthly|forecast|growth)/i.test(endpointPath)) {
    return <div className="chart-card"><h3>{title}</h3><ResponsiveContainer width="100%" height={400}>
      <LineChart data={data}><CartesianGrid strokeDasharray="3 3" /><XAxis dataKey={categoryKey} /><YAxis tickFormatter={tick} />
        <Tooltip formatter={tooltipFormatter} /><Legend />
        {numericKeys.map((k, i) => <Line key={k} type="monotone" dataKey={k} stroke={COLORS[i % COLORS.length]} strokeWidth={3} dot={false} />)}
      </LineChart>
    </ResponsiveContainer></div>;
  }

  if (/(collections|reimbursement|expected)/i.test(endpointPath) && numericKeys.length > 1) {
    return <div className="chart-card"><h3>{title}</h3><ResponsiveContainer width="100%" height={400}>
      <AreaChart data={data}><CartesianGrid strokeDasharray="3 3" /><XAxis dataKey={categoryKey} /><YAxis tickFormatter={tick} />
        <Tooltip formatter={tooltipFormatter} /><Legend />
        {numericKeys.map((k, i) => <Area key={k} type="monotone" dataKey={k} stroke={COLORS[i % COLORS.length]} fill={COLORS[i % COLORS.length]} fillOpacity={0.18} />)}
      </AreaChart>
    </ResponsiveContainer></div>;
  }

  return <div className="chart-card"><h3>{title}</h3><ResponsiveContainer width="100%" height={420}>
    <BarChart data={data} layout={data.length >= 8 ? 'vertical' : 'horizontal'}>
      <CartesianGrid strokeDasharray="3 3" />
      {data.length >= 8 ? <><XAxis type="number" tickFormatter={tick}/><YAxis type="category" dataKey={categoryKey} width={145}/></> : <><XAxis dataKey={categoryKey}/><YAxis tickFormatter={tick}/></>}
      <Tooltip formatter={tooltipFormatter} /><Legend />
      {numericKeys.map((k, i) => <Bar key={k} dataKey={k} fill={COLORS[i % COLORS.length]} radius={[5,5,0,0]} />)}
    </BarChart>
  </ResponsiveContainer></div>;
}
