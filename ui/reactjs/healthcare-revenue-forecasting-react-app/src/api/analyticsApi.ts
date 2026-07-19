import { httpClient } from './httpClient';
import type { AnalyticsResponse, ApiValue } from '../types/api';

export async function getAnalytics(module: string, path: string, params?: Record<string, number>): Promise<AnalyticsResponse> {
  const url = `/${module}${path === '/' ? '' : path}`;
  if (path.endsWith('/chart')) {
    const response = await httpClient.get<Blob>(url, { params, responseType: 'blob' });
    return { kind: 'image', data: URL.createObjectURL(response.data) };
  }
  const response = await httpClient.get<ApiValue>(url, { params });
  return { kind: 'json', data: response.data };
}
