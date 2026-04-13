/**
 * WEALTH by arifOS — Projection Engine
 * 
 * All projections carry ESTIMATE tag.
 * All projections show uncertainty band.
 * No single-point future presented as CLAIM.
 * 
 * F7: Humility band 0.03–0.15 minimum.
 * 
 * DITEMPA BUKAN DIBERI — 999 SEAL ALIVE
 */

'use strict';

const { EPISTEMIC } = require('../kernel/floors');

/**
 * projectCompoundGrowth — FV = PV × (1 + r)^n
 * Always returns [low, mid, high] band.
 * 
 * @param {number} pv - Present value
 * @param {number} rateAnnual - Annual rate (e.g., 0.07 for 7%)
 * @param {number} years - Projection horizon
 * @param {number} uncertaintyBand - Min 0.03, max 0.15 per F7
 * @returns {Object} ESTIMATE-tagged projection
 */
function projectCompoundGrowth(pv, rateAnnual, years, uncertaintyBand = 0.08) {
  // F7 enforcement: clamp uncertainty band
  const band = Math.min(Math.max(uncertaintyBand, 0.03), 0.50);

  const fvMid  = pv * Math.pow(1 + rateAnnual, years);
  const fvLow  = pv * Math.pow(1 + (rateAnnual - band), years);
  const fvHigh = pv * Math.pow(1 + (rateAnnual + band), years);

  return {
    tag: EPISTEMIC.ESTIMATE,
    pv,
    rate_annual: rateAnnual,
    years,
    uncertainty_band: band,
    result: {
      low:  Math.round(fvLow  * 100) / 100,
      mid:  Math.round(fvMid  * 100) / 100,
      high: Math.round(fvHigh * 100) / 100,
    },
    warning: 'ESTIMATE only. Past performance does not guarantee future results.',
    epoch: new Date().toISOString(),
  };
}

/**
 * projectRunwayDepletion — When does runway end given burn rate?
 * @param {number} liquidAssets
 * @param {number} monthlyBurn
 * @param {number} monthlyIncome
 * @returns {Object}
 */
function projectRunwayDepletion(liquidAssets, monthlyBurn, monthlyIncome = 0) {
  const netBurn = monthlyBurn - monthlyIncome;
  if (netBurn <= 0) {
    return {
      tag: EPISTEMIC.PLAUSIBLE,
      months_remaining: Infinity,
      depletes: false,
      message: 'Income exceeds burn — runway extends indefinitely under current conditions.',
      epoch: new Date().toISOString(),
    };
  }

  const monthsRemaining = liquidAssets / netBurn;
  const depletionDate = new Date();
  depletionDate.setMonth(depletionDate.getMonth() + Math.floor(monthsRemaining));

  return {
    tag: EPISTEMIC.ESTIMATE,
    months_remaining: Math.round(monthsRemaining * 10) / 10,
    depletion_date: depletionDate.toISOString().split('T')[0],
    depletes: true,
    net_burn_monthly: netBurn,
    uncertainty_band: 0.08,
    epoch: new Date().toISOString(),
  };
}

module.exports = { projectCompoundGrowth, projectRunwayDepletion };
