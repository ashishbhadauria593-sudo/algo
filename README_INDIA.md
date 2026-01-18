India (NSE) Quick Start
========================

This project contains a small helper and a sample CSV for quick demos of Indian instruments (NSE options/futures).

Sample CSV path: `backtesting/test/NSE_SAMPLE_OPTION.csv`

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
            self.buy(size=1)

# Load the bundled sample CSV and run a tiny demo
df = load_nse_csv(r'backtesting\\test\\NSE_SAMPLE_OPTION.csv', datetime_col='Date')
mc = MarketConfig(is_derivative=True, lot_size=1)
bt = Backtest(df, ExampleOptionsStrategy, cash=100000, market_config=mc, finalize_trades=True)
print(bt.run())
PY
```

Notes:
- The demo localizes timestamps to Asia/Kolkata.
- `MarketConfig` allows setting `is_derivative`, `lot_size`, trading hours and holidays.
- The sample CSV is synthetic and intended for quick testing only; replace it with real data for realistic results.
