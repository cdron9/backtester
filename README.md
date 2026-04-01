# Custom Backtester

A backtesting engine for a moving average crossover strategy, tested against 2 years of AAPL historical data.

Built as Project 2 of a self-directed quant finance curriculum.

---

## What it does

- Pulls 2 years of OHLCV data for AAPL via yfinance
- Calculates 20 and 50 day moving averages
- Detects golden cross (buy) and death cross (sell) signals using boolean logic and pandas `.shift()` for day-over-day comparison
- Pairs each buy signal with the next chronological sell signal to form complete trades
- Stores each trade as a dictionary containing entry date, entry price, exit date, exit price, and profit
- Outputs a results DataFrame with total P&L
- Visualizes price action, moving averages, and buy/sell signals on a single chart

---

## How to run

1. Clone the repo
2. Create and activate a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
```
3. Install dependencies:
```bash
   pip install -r requirements.txt
```
4. Run:
```bash
   python main.py
```

---

## What I learned

- How to generate trading signals using boolean logic across pandas DataFrames
- How `.shift()` enables day-over-day comparisons to detect crossover events
- How to pair buy and sell signals chronologically to simulate real trades
- How to store and structure trade results using a list of dictionaries converted to a DataFrame
- Why backtests can be misleading — this model ignores slippage and fees which would worsen the real world P&L
- That an intuitive strategy does not guarantee edge — the MA crossover lost money on AAPL over this period

---

## Notes

This backtester is intentionally simplified. Real world performance would differ due to:

- **Slippage** — fills rarely occur at the exact closing price
- **Commission/fees** — broker costs on every buy and sell eat into P&L
- **Single ticker** — tested only on AAPL, results will vary across different stocks and market conditions
- **Lookahead bias** — using closing price as entry assumes you can trade at close, which isn't always possible
- **No position sizing** — assumes a fixed single share per trade, real strategies size positions based on portfolio risk
