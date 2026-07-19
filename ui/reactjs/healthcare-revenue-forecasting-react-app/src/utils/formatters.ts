export const titleize = (value: string) => value.replace(/[_-]/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
export const formatValue = (value: unknown) => {
  if (typeof value === 'number') return value.toLocaleString(undefined, { maximumFractionDigits: 2 });
  if (value === null || value === undefined) return '—';
  return String(value);
};
export const isMoneyKey = (key: string) => /(revenue|amount|balance|payment|collection|cost|charge|billing|ar|leakage)/i.test(key);
