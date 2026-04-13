/**
 * WEALTH by arifOS — Net Worth Engine
 * 
 * NetWorth = Σ(assets) − Σ(liabilities)
 * Physics. Non-negotiable.
 * 
 * DITEMPA BUKAN DIBERI — 999 SEAL ALIVE
 */

'use strict';

const { EPISTEMIC, checkFloors } = require('../kernel/floors');

/**
 * computeNetWorth — Core calculation
 * @param {Array} assets
 * @param {Array} liabilities
 * @returns {{ netWorth: number, tag: string, assetTotal: number, liabilityTotal: number, breakdown: Object }}
 */
function computeNetWorth(assets = [], liabilities = []) {
  // F9: Anti-Hantu — filter out deleted/unresolved
  const activeAssets = assets.filter(a => !a.deleted);
  const activeLiabilities = liabilities.filter(l => !l.deleted);

  const assetTotal = activeAssets.reduce((sum, a) => sum + (a.value ?? 0), 0);
  const liabilityTotal = activeLiabilities.reduce((sum, l) => sum + (l.principal ?? 0), 0);
  const netWorth = assetTotal - liabilityTotal;

  // Epistemic degradation: if any input is ESTIMATE, output is ESTIMATE
  const allTags = [
    ...activeAssets.map(a => a.tag),
    ...activeLiabilities.map(l => l.tag),
  ];
  const tag = allTags.some(t => t === EPISTEMIC.ESTIMATE || t === EPISTEMIC.HYPOTHESIS)
    ? EPISTEMIC.ESTIMATE
    : allTags.some(t => t === EPISTEMIC.UNKNOWN)
    ? EPISTEMIC.UNKNOWN
    : EPISTEMIC.CLAIM;

  return {
    netWorth,
    tag,
    assetTotal,
    liabilityTotal,
    breakdown: {
      assets: activeAssets,
      liabilities: activeLiabilities,
    },
    epoch: new Date().toISOString(),
  };
}

/**
 * netWorthDelta — Detect significant changes. Triggers 888 HOLD if > -20%.
 * @param {number} previous
 * @param {number} current
 * @returns {{ delta: number, deltaPercent: number, hold: boolean }}
 */
function netWorthDelta(previous, current) {
  if (previous === 0) return { delta: current, deltaPercent: null, hold: false };
  const delta = current - previous;
  const deltaPercent = (delta / Math.abs(previous)) * 100;
  const hold = deltaPercent < -20; // 888 HOLD if >20% drop in a session

  return { delta, deltaPercent, hold };
}

module.exports = { computeNetWorth, netWorthDelta };
