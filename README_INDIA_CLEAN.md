# India (NSE) Quick Start

This repository includes small helpers and a bundled sample CSV for quick demos of Indian instruments (NSE options/futures).

Bundled sample CSV (synthetic): `backtesting/test/NSE_SAMPLE_OPTION.csv`

Quick run (PowerShell, from project root):

```powershell
cd .\backtesting.py
python - <<'PY'
from backtesting.data_india import load_nse_csv
from backtesting.market_india import MarketConfig
from backtesting.backtesting import Backtest, Strategy

class ExampleOptionsStrategy(Strategy):
    def init(self): pass
    def next(self):
        if not self.position and len(self.data.Close) > 1:
            # Request one lot from MarketConfig
            lot = self._bt.market_config.lot_size if getattr(self._bt, 'market_config', None) else 1
            try:
                self.buy(size=lot)
            except ValueError:
                return

# Load the bundled sample CSV and run a tiny demo
# (the loader localizes timestamps to Asia/Kolkata)

df = load_nse_csv(r'backtesting\\test\\NSE_SAMPLE_OPTION.csv')
mc = MarketConfig(is_derivative=True, lot_size=75, tick_size=0.05)
bt = Backtest(df, ExampleOptionsStrategy, cash=100000, market_config=mc)
print(bt.run())
PY
```

Notes:
- Timestamps are localized to Asia/Kolkata by `load_nse_csv`.
- `MarketConfig` options:
  - `is_derivative`: set to True for F&O instruments (enables lot enforcement).
  - `lot_size`: number of underlying units per contract (broker enforces multiples).
  - `tick_size`: minimum price increment (prices are rounded to nearest tick).
  - trading hours and holidays can be customized via `MarketConfig`.

- The bundled CSV is synthetic and intended for quick testing only; replace it with real contract data for realistic results.

For code-level docs, see `backtesting/market_india.py` and `backtesting/data_india.py`.
