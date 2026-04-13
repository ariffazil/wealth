/**
 * WEALTH by arifOS — Maruah Score Engine
 * 
 * Maruah = Dignity. A real financial variable.
 * Range: 0.0 – 1.0. Floor: 0.6 (configurable).
 * 
 * F6: ASEAN/MY context — includes amanah, zakat-alignment, sovereignty.
 * 
 * DITEMPA BUKAN DIBERI — 999 SEAL ALIVE
 */

'use strict';

const DEFAULT_FLOOR = 0.6;

/**
 * computeMaruahScore — Composite dignity/integrity score
 * 
 * Dimensions:
 * - financial_integrity: Are all numbers honest and tagged? (0–1)
 * - sovereignty: Is financial data under human control? (0–1)
 * - debt_dignity: Is debt within honourable limits? (0–1)
 * - amanah_index: Trust/stewardship signals (0–1) [MY/ASEAN context]
 * - community_contribution: Zakat, sedekah, or equivalent (0–1)
 * 
 * @param {Object} params
 * @returns {{ score: number, dimensions: Object, floor: number, below_floor: boolean, tag: string }}
 */
function computeMaruahScore(params = {}) {
  const {
    financial_integrity = 0.5,
    sovereignty = 0.5,
    debt_dignity = 0.5,
    amanah_index = 0.5,
    community_contribution = 0.0,
    floor = DEFAULT_FLOOR,
  } = params;

  // Weighted composite — integrity and sovereignty weighted highest
  const score =
    (financial_integrity * 0.30) +
    (sovereignty         * 0.25) +
    (debt_dignity        * 0.20) +
    (amanah_index        * 0.15) +
    (community_contribution * 0.10);

  const rounded = Math.round(score * 100) / 100;

  return {
    score: rounded,
    dimensions: {
      financial_integrity,
      sovereignty,
      debt_dignity,
      amanah_index,
      community_contribution,
    },
    floor,
    below_floor: rounded < floor,
    hold_triggered: rounded < floor, // 888 HOLD if below floor
    tag: 'ESTIMATE', // Always ESTIMATE — dignity cannot be fully quantified
    epoch: new Date().toISOString(),
  };
}

/**
 * interpretMaruahScore — Human-readable interpretation
 */
function interpretMaruahScore(score) {
  if (score >= 0.85) return { band: 'SOVEREIGN',   label: 'Kedaulatan penuh — wealth with full dignity' };
  if (score >= 0.70) return { band: 'STABLE',      label: 'Stabil — good integrity, room to grow' };
  if (score >= 0.60) return { band: 'FLOOR',       label: 'At floor — monitor closely' };
  if (score >= 0.40) return { band: 'AMBER',       label: 'Warning — dignity compromised in some dimensions' };
  return                     { band: 'RED',         label: '888 HOLD — urgent review required' };
}

module.exports = { computeMaruahScore, interpretMaruahScore, DEFAULT_FLOOR };
