/**
 * WEALTH OS — Public API Exports
 * DITEMPA BUKAN DIBERI — 999 SEAL ALIVE
 */

// Kernel
export { FLOORS, EPISTEMIC, HOLD, checkFloors, assertFloors } from './kernel/floors.js';
export { STAGES, runPipeline } from './kernel/pipeline.js';
export { seal999 } from './kernel/seal.js';
export { emitTelemetry } from './kernel/telemetry.js';
export { initVault999, appendVault999 } from './kernel/vault999.js';
export { calculateRiskAdjustedRate } from './kernel/capitalx.js';

// Wealth Domain
export { computeNetWorth, netWorthDelta } from './wealth/networth.js';
export { computeCashflow, EXPENSE_CATEGORIES, INCOME_RELIABILITY } from './wealth/cashflow.js';
export { computeMaruahScore, interpretMaruahScore, DEFAULT_FLOOR } from './wealth/maruah-score.js';
export { projectCompoundGrowth, projectRunwayDepletion } from './wealth/projection.js';
