from operator import index
from pandas._libs.hashtable import value_count
import yfinance as yf 
import pandas as pd 
import matplotlib.pyplot as plt 

trades = []

ticker = yf.Ticker("AAPL")
df = ticker.history(period="2y")

df["MA20"] = df["Close"].rolling(window=20).mean()
df["MA50"] = df["Close"].rolling(window=50).mean()

gold_today = df["MA20"] > df["MA50"]
gold_yesterday = df["MA20"].shift(1) < df["MA50"].shift(1)

death_today = df["MA20"] < df["MA50"] 
death_yesterday = df["MA20"].shift(1) > df["MA50"].shift(1)


df["golden_cross"] = gold_today & gold_yesterday
df["death_cross"] = death_today & death_yesterday


buy_signals = df[df["golden_cross"] == True]["Close"]
sell_signals = df[df["death_cross"] == True]["Close"]


for buy_date, buy_price in buy_signals.items():
    future_sells = sell_signals[sell_signals.index > buy_date]

    if len(future_sells) == 0:
        continue

    sell_date = future_sells.index[0]
    sell_price = future_sells.iloc[0]

    profit = sell_price - buy_price

    trades.append({
        "entry_date": buy_date,
        "entry_price": buy_price, 
        "exit_date": sell_date,
        "exit_price": sell_price,
        "profit": profit
    })

results = pd.DataFrame(trades)
print(results.to_string())
print(f"Total P&L: {results['profit'].sum():.2f}")

fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(df.index, df["Close"], label="Close", alpha=0.5)
ax.plot(df.index, df["MA20"], label="MA20")
ax.plot(df.index, df["MA50"], label="MA50")

ax.scatter(buy_signals.index, buy_signals.values, marker="^", color="green", zorder=5, label="Buy")
ax.scatter(sell_signals.index, sell_signals.values, marker="v", color="red", zorder=5, label="Sell")

ax.legend()
ax.set_title("AAPL MA Crossover Strategy")
ax.set_ylabel("Price (USD)")
plt.tight_layout()
plt.show()
