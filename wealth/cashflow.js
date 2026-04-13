/**
 * WEALTH by arifOS — Cashflow Engine
 * 
 * Cashflow = Income − Expenses
 * Runway = Liquid Assets / Monthly Burn
 * 
 * DITEMPA BUKAN DIBERI — 999 SEAL ALIVE
 */

'use strict';

const { EPISTEMIC } = require('../kernel/floors');

const EXPENSE_CATEGORIES = {
  FIXED:         'fixed',
  VARIABLE:      'variable',
  DISCRETIONARY: 'discretionary',
  EMERGENCY:     'emergency',
};

const INCOME_RELIABILITY = {
  GUARANTEED: 'guaranteed',  // CLAIM
  REGULAR:    'regular',     // PLAUSIBLE
  IRREGULAR:  'irregular',   // ESTIMATE
  SPECULATIVE: 'speculative', // HYPOTHESIS
};

/**
 * computeCashflow — Monthly cashflow
 * @param {Array} income - Income streams
 * @param {Array} expenses - Expense items
 * @returns {{ monthlyIncome, monthlyExpenses, monthlyCashflow, tag, runway }}
 */
function computeCashflow(income = [], expenses = [], liquidAssets = 0) {
  const activeIncome = income.filter(i => !i.deleted && i.active !== false);
  const activeExpenses = expenses.filter(e => !e.deleted);

  const monthlyIncome = activeIncome.reduce((sum, i) => sum + (i.monthly_amount ?? 0), 0);
  const monthlyExpenses = activeExpenses.reduce((sum, e) => sum + (e.monthly_amount ?? 0), 0);
  const monthlyCashflow = monthlyIncome - monthlyExpenses;

  // Runway: how many months of liquid assets at current burn
  const monthlyBurn = activeExpenses
    .filter(e => e.category === EXPENSE_CATEGORIES.FIXED || e.category === EXPENSE_CATEGORIES.VARIABLE)
    .reduce((sum, e) => sum + (e.monthly_amount ?? 0), 0);

  const runway = monthlyBurn > 0 ? liquidAssets / monthlyBurn : Infinity;

  // Epistemic tag
  const hasSpeculative = activeIncome.some(i => i.reliability === INCOME_RELIABILITY.SPECULATIVE);
  const hasIrregular = activeIncome.some(i => i.reliability === INCOME_RELIABILITY.IRREGULAR);
  const tag = hasSpeculative
    ? EPISTEMIC.HYPOTHESIS
    : hasIrregular
    ? EPISTEMIC.ESTIMATE
    : EPISTEMIC.PLAUSIBLE;

  return {
    monthlyIncome,
    monthlyExpenses,
    monthlyCashflow,
    monthlyBurn,
    runway: Math.round(runway * 10) / 10,
    tag,
    epoch: new Date().toISOString(),
  };
}

module.exports = { computeCashflow, EXPENSE_CATEGORIES, INCOME_RELIABILITY };
