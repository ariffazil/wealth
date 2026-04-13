/**
 * WEALTH by arifOS — capitalx_risk_pricing_engine
 *
 * Translates constitutional signals into cost-of-capital adjustments.
 * When entropy-bounded actors borrow cheaper, markets migrate toward them.
 * DITEMPA BUKAN DIBERI — 999 SEAL ALIVE
 */

/**
 * Calculate risk-adjusted cost of capital from WEALTH constitutional signals.
 * @param {number} baseRate - Starting interest rate (e.g., 0.05 for 5%)
 * @param {Object} signals - Constitutional metrics
 * @param {number} signals.dS - Entropy delta (≥0 increases cost)
 * @param {number} signals.peace2 - Peace score (≥1.0 reduces cost)
 * @param {number} signals.maruahScore - Maruah dignity score (0–1)
 * @param {number} signals.trustIndex - Trust topology score (0–1)
 * @param {number} signals.deltaCiv - Civilization stability delta
 * @returns {Object} Risk-adjusted rate breakdown
 */
export function calculateRiskAdjustedRate(baseRate, signals) {
  const { dS, peace2, maruahScore, trustIndex, deltaCiv } = signals;

  // Entropy penalty: higher disorder increases borrowing cost
  const entropyPenalty = Math.max(0, (dS ?? 0) * 0.5);

  // Peace discount: calm systems are cheaper to finance
  const peaceDiscount = Math.min(0.02, Math.max(0, ((peace2 ?? 1.0) - 1.0) * 0.05));

  // Maruah discount: dignity reduces moral hazard and default risk
  const maruahDiscount = Math.min(0.03, Math.max(0, ((maruahScore ?? 0.5) - 0.5) * 0.06));

  // Trust discount: verified networks lower coordination premiums
  const trustDiscount = Math.min(0.02, Math.max(0, ((trustIndex ?? 0.5) - 0.5) * 0.04));

  // Civilization bonus: positive ΔCiv signals long-horizon resilience
  const civDiscount = Math.min(0.02, Math.max(0, ((deltaCiv ?? 0) * 0.1)));

  const adjusted = baseRate + entropyPenalty - peaceDiscount - maruahDiscount - trustDiscount - civDiscount;

  return {
    base_rate: baseRate,
    adjusted_rate: Math.max(0, Number(adjusted.toFixed(6))),
    adjustments: {
      entropy_penalty: Number(entropyPenalty.toFixed(6)),
      peace_discount: Number(peaceDiscount.toFixed(6)),
      maruah_discount: Number(maruahDiscount.toFixed(6)),
      trust_discount: Number(trustDiscount.toFixed(6)),
      civ_discount: Number(civDiscount.toFixed(6)),
    },
    tag: 'ESTIMATE',
    epoch: new Date().toISOString(),
  };
}

/**
 * Compare two capital nodes and return the WEALTH advantage in basis points.
 * @param {number} baseRate
 * @param {Object} wealthSignals
 * @param {Object} extractiveSignals
 * @returns {{ advantage_bps: number, wealth_rate: number, extractive_rate: number }}
 */
export function compareCapitalAdvantage(baseRate, wealthSignals, extractiveSignals) {
  const wealth = calculateRiskAdjustedRate(baseRate, wealthSignals);
  const extractive = calculateRiskAdjustedRate(baseRate, extractiveSignals);
  const advantage_bps = Math.round((extractive.adjusted_rate - wealth.adjusted_rate) * 10000);

  return {
    advantage_bps,
    wealth_rate: wealth.adjusted_rate,
    extractive_rate: extractive.adjusted_rate,
    wealth_result: wealth,
    extractive_result: extractive,
    tag: 'ESTIMATE',
    epoch: new Date().toISOString(),
  };
}
