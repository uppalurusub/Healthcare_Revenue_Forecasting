import type { ApiValue, ChartModel } from '../types/api';

const objectRows = (value: ApiValue): Record<string, unknown>[] | null => {
  if (Array.isArray(value) && value.length && value.every(v => v && typeof v === 'object' && !Array.isArray(v))) {
    return value as Record<string, unknown>[];
  }
  if (value && typeof value === 'object' && !Array.isArray(value)) {
    for (const nested of Object.values(value)) {
      const rows = objectRows(nested);
      if (rows) return rows;
    }
  }
  return null;
};

export function toChartModel(value: ApiValue): ChartModel | null {
  const rows = objectRows(value);
  if (!rows || rows.length < 2) return null;
  const keys = Array.from(new Set(rows.flatMap(row => Object.keys(row))));
  const numericKeys = keys.filter(key => rows.some(row => typeof row[key] === 'number')).slice(0, 4);
  if (!numericKeys.length) return null;
  const categoryKey = keys.find(key => !numericKeys.includes(key) && rows.some(row => typeof row[key] === 'string')) ?? keys[0];
  return { data: rows, categoryKey, numericKeys };
}
