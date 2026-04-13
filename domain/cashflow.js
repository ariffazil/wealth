/**
 * WEALTH Domain: Cashflow Engine
 * Enforces F9 Anti-Hantu (Grounding) via CLAIM/PLAUSIBLE tagging.
 */
export function processTransaction(entry) {
  if (!["CLAIM", "PLAUSIBLE", "ESTIMATE"].includes(entry.tag)) {
    throw new Error("F9 Violation: Unverified financial entry (Hantu detected)");
  }
  
  return {
    ...entry,
    processedAt: new Date().toISOString(),
    status: "SEALED"
  };
}

export function calculateRunway(cash, monthlyBurn) {
  return {
    months: monthlyBurn > 0 ? (cash / monthlyBurn).toFixed(1) : Infinity,
    risk: monthlyBurn > cash ? "CRITICAL" : "STABLE"
  };
}
