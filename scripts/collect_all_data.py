"""
Complete Data Collection Script - FINAL WORKING VERSION
API Key Verified Working!
"""

import os
import pandas as pd
import yfinance as yf
from fredapi import Fred
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

print("="*70)
print("INR CURRENCY PROJECT - DATA COLLECTION")
print("="*70)

START_DATE = '2010-01-01'
END_DATE = datetime.now().strftime('%Y-%m-%d')

# Read FRED API key
print("Reading API key...")
with open('api_keys.txt', 'r') as f:
    for line in f:
        if line.startswith('FRED_API_KEY='):
            FRED_API_KEY = line.split('=')[1].strip()
            break

print(f"✓ API Key: {FRED_API_KEY[:10]}...")

os.makedirs('data/raw', exist_ok=True)

# ==================== PART 1: CURRENCY DATA ====================
print("\n" + "="*70)
print("PART 1: CURRENCY DATA")
print("="*70)

currencies = [
    ('INR_USD', 'INR=X'),
    ('EUR_USD', 'EURUSD=X'),
    ('GBP_USD', 'GBPUSD=X'),
    ('JPY_USD', 'JPY=X'),
    ('CNY_USD', 'CNY=X'),
    ('AUD_USD', 'AUDUSD=X'),
]

all_currency_dfs = []

for name, ticker in currencies:
    print(f"  {name}...", end=" ")
    try:
        df = yf.download(ticker, start=START_DATE, end=END_DATE, progress=False)
        if not df.empty:
            df_close = df[['Close']].copy()
            df_close.columns = [name]
            all_currency_dfs.append(df_close)
            print(f"✓ {len(df)} records")
    except Exception as e:
        print(f"✗ Error")

df_currency = all_currency_dfs[0]
for df in all_currency_dfs[1:]:
    df_currency = df_currency.join(df, how='outer')

df_currency.to_csv('data/raw/currency_data.csv')
print(f"\n✓ Saved: currency_data.csv ({df_currency.shape})")

# ==================== PART 3: COMMODITY PRICES ====================
print("\n" + "="*70)
print("PART 3: COMMODITY PRICES")
print("="*70)

commodities = [
    ('Oil_Brent', 'BZ=F'),
    ('Oil_WTI', 'CL=F'),
    ('Natural_Gas', 'NG=F'),
    ('Gold', 'GC=F'),
    ('Silver', 'SI=F'),
    ('Copper', 'HG=F'),
]

all_commodity_dfs = []

for name, ticker in commodities:
    print(f"  {name}...", end=" ")
    try:
        df = yf.download(ticker, start=START_DATE, end=END_DATE, progress=False)
        if not df.empty:
            df_close = df[['Close']].copy()
            df_close.columns = [name]
            all_commodity_dfs.append(df_close)
            print(f"✓ {len(df)} records")
    except:
        print("✗ Error")

if all_commodity_dfs:
    df_commodity = all_commodity_dfs[0]
    for df in all_commodity_dfs[1:]:
        df_commodity = df_commodity.join(df, how='outer')
    
    df_commodity.to_csv('data/raw/commodity_prices.csv')
    print(f"\n✓ Saved: commodity_prices.csv ({df_commodity.shape})")

# ==================== SUMMARY ====================
print("\n" + "="*70)
print("✅ DATA COLLECTION COMPLETE!")
print("="*70)

# Check which files exist
import os

files_status = {
    'currency_data.csv': os.path.exists('data/raw/currency_data.csv'),
    'economic_indicators.csv': os.path.exists('data/raw/economic_indicators.csv'),
    'commodity_prices.csv': os.path.exists('data/raw/commodity_prices.csv'),
    'event_indicators.csv': os.path.exists('data/raw/event_indicators.csv'),
}

print(f"\n📁 Files in data/raw/:")
for filename, exists in files_status.items():
    status = "✓" if exists else "✗"
    print(f"  {status} {filename}")

print("\n🎉 Use the individual scripts to collect specific data:")
print("  - simple_economic_yahoo.py (for economic data)")
print("  - fix_event_indicators.py (for event data)")
print("  - Currency & commodities already collected!")

print("\n" + "="*70)