import type { ApiValue, ApiObject } from '../types/api';
import { formatValue, titleize } from '../utils/formatters';

export function DataRenderer({ data }: { data: ApiValue }) {
  if (Array.isArray(data)) {
    if (!data.length) return <div className="empty">No records returned.</div>;
    if (data.every(v => v && typeof v === 'object' && !Array.isArray(v))) {
      const rows = data as ApiObject[];
      const columns = Array.from(new Set(rows.flatMap(row => Object.keys(row))));
      return <div className="table-wrap"><table><thead><tr>{columns.map(c => <th key={c}>{titleize(c)}</th>)}</tr></thead><tbody>
        {rows.map((row,i) => <tr key={i}>{columns.map(c => <td key={c}>{typeof row[c] === 'object' && row[c] !== null ? <DataRenderer data={row[c]} /> : formatValue(row[c])}</td>)}</tr>)}
      </tbody></table></div>;
    }
    return <div>{data.map((v,i) => <DataRenderer key={i} data={v}/>)}</div>;
  }
  if (data && typeof data === 'object') {
    return <div className="metric-grid">{Object.entries(data).map(([k,v]) => typeof v === 'object' && v !== null
      ? <section className="nested-card" key={k}><h3>{titleize(k)}</h3><DataRenderer data={v}/></section>
      : <div className="metric" key={k}><span>{titleize(k)}</span><strong>{formatValue(v)}</strong></div>)}</div>;
  }
  return <span>{formatValue(data)}</span>;
}
