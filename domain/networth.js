/**
 * WEALTH Domain: Net Worth Engine
 */

export function calculateNetWorth(assets, liabilities) {
  const totalAssets = assets.reduce((sum, a) => sum + a.value, 0);
  const totalLiabilities = liabilities.reduce((sum, l) => sum + l.value, 0);
  
  return {
    netWorth: totalAssets - totalLiabilities,
    ratio: totalLiabilities > 0 ? totalAssets / totalLiabilities : Infinity,
    timestamp: Date.now()
  };
}
