import yfinance as yf 
import pandas as pd 
import matplotlib.pyplot as plt 

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

print(buy_signals, sell_signals)
