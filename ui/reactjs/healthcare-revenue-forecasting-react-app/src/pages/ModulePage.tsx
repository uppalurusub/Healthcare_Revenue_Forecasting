import { useEffect, useMemo, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getAnalytics } from '../api/analyticsApi';
import { AnalyticsChart } from '../components/charts/AnalyticsChart';
import { DataRenderer } from '../components/DataRenderer';
import { ENDPOINTS } from '../config/endpoints';
import type { AnalyticsResponse } from '../types/api';
import { toChartModel } from '../utils/chartAdapter';
import { titleize } from '../utils/formatters';

export function ModulePage() {
  const { module = 'dashboard' } = useParams();
  const endpoints = ENDPOINTS[module] ?? [];
  const [selected, setSelected] = useState(0);
  const [response, setResponse] = useState<AnalyticsResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  useEffect(() => setSelected(0), [module]);
  const endpoint = endpoints[selected];

  useEffect(() => {
    if (!endpoint) return;
    let active = true; let imageUrl: string | undefined;
    setLoading(true); setError(''); setResponse(null);
    getAnalytics(module, endpoint.path, endpoint.params).then(result => {
      if (!active) { if (result.kind === 'image') URL.revokeObjectURL(result.data); return; }
      if (result.kind === 'image') imageUrl = result.data;
      setResponse(result);
    }).catch(e => active && setError(e instanceof Error ? e.message : 'Unable to load analytics'))
      .finally(() => active && setLoading(false));
    return () => { active = false; if (imageUrl) URL.revokeObjectURL(imageUrl); };
  }, [module, endpoint]);

  const chartModel = useMemo(() => response?.kind === 'json' ? toChartModel(response.data) : null, [response]);

  return <main className="content"><header><p className="eyebrow">Healthcare Revenue Cycle</p><h1>{titleize(module)}</h1></header>
    <div className="tabs">{endpoints.map((e,i) => <button key={`${e.path}-${i}`} className={selected===i?'selected':''} onClick={() => setSelected(i)}>{e.label}</button>)}</div>
    <section className="panel">
      {loading ? <div className="state">Loading analytics…</div> : error ? <div className="error">{error}</div> :
       response?.kind === 'image' ? <div className="chart-card"><h3>{endpoint?.label}</h3><img className="api-chart" src={response.data} alt={endpoint?.label}/></div> :
       response?.kind === 'json' ? <><DataRenderer data={response.data}/>{chartModel && <AnalyticsChart model={chartModel} endpointPath={endpoint.path} title={`${endpoint.label} Visualization`}/>}</> : null}
    </section>
  </main>;
}
