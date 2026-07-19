export type Primitive = string | number | boolean | null;
export type ApiValue = Primitive | ApiObject | ApiValue[];
export interface ApiObject { [key: string]: ApiValue }
export interface EndpointDefinition { path: string; label: string; params?: Record<string, number> }
export type AnalyticsResponse = { kind: 'json'; data: ApiValue } | { kind: 'image'; data: string };
export interface ChartModel {
  data: Record<string, unknown>[];
  categoryKey: string;
  numericKeys: string[];
}
