"""
Simple Economic Data Collection - ONLY using yfinance (already installed)
NO pandas_datareader needed!
"""

import pandas as pd
import yfinance as yf
from datetime import datetime

print("="*70)
print("COLLECTING ECONOMIC DATA FROM YAHOO FINANCE")
print("="*70)

START_DATE = '2010-01-01'
END_DATE = datetime.now().strftime('%Y-%m-%d')

print(f"\nDate range: {START_DATE} to {END_DATE}")

# Economic indicators available on Yahoo Finance
indicators = {
    'VIX': '^VIX',                    # Volatility Index (Fear gauge)
    'SP500': '^GSPC',                 # S&P 500 Index
    'DXY': 'DX=F',                    # US Dollar Index
    'US_10Y_Treasury': '^TNX',        # 10-Year Treasury Yield
    'Nasdaq': '^IXIC',                # Nasdaq Index
    'Dow_Jones': '^DJI',              # Dow Jones Index
}

print(f"\nDownloading {len(indicators)} indicators...\n")

all_dfs = []
success_count = 0

for name, ticker in indicators.items():
    print(f"  {name} ({ticker})...", end=" ", flush=True)
    
    try:
        # Download data
        df = yf.download(ticker, start=START_DATE, end=END_DATE, progress=False)
        
        if not df.empty and 'Close' in df.columns:
            # Extract Close price and rename column
            df_close = df[['Close']].copy()
            df_close.columns = [name]
            all_dfs.append(df_close)
            success_count += 1
            print(f"✓ {len(df):,} records")
        else:
            print("✗ Empty or no Close column")
            
    except Exception as e:
        print(f"✗ Error: {str(e)[:40]}")

# Combine all dataframes
if all_dfs:
    print(f"\n✓ Successfully downloaded {success_count}/{len(indicators)} indicators")
    
    # Start with first dataframe
    df_economic = all_dfs[0]
    
    # Join the rest
    for df in all_dfs[1:]:
        df_economic = df_economic.join(df, how='outer')
    
    # Save to CSV
    output_path = 'data/raw/economic_indicators.csv'
    df_economic.to_csv(output_path)
    
    print(f"\n{'='*70}")
    print("✅ SUCCESS!")
    print(f"{'='*70}")
    
    print(f"\n📄 Saved: {output_path}")
    print(f"  Shape: {df_economic.shape[0]:,} rows × {df_economic.shape[1]} columns")
    print(f"  Date range: {df_economic.index[0].date()} to {df_economic.index[-1].date()}")
    
    print(f"\n📊 Columns:")
    for col in df_economic.columns:
        non_null = df_economic[col].notna().sum()
        pct_filled = (non_null / len(df_economic)) * 100
        print(f"  • {col}: {non_null:,} values ({pct_filled:.1f}% complete)")
    
    print(f"\n🔍 First 5 rows:")
    print(df_economic.head())
    
    print(f"\n📈 Sample values (most recent):")
    latest = df_economic.iloc[-1]
    for col in df_economic.columns:
        if pd.notna(latest[col]):
            print(f"  {col}: {latest[col]:.2f}")
    
    print(f"\n{'='*70}")
    print("🎉 Economic data collection COMPLETE!")
    print(f"{'='*70}")
    
    print("\n✅ You now have:")
    print("  1. currency_data.csv")
    print("  2. commodity_prices.csv")
    print("  3. event_indicators.csv")
    print("  4. economic_indicators.csv")
    print("\n🚀 Ready for Week 2 - Data Analysis!")
    
else:
    print(f"\n{'='*70}")
    print("❌ FAILED - No data collected")
    print(f"{'='*70}")
    print("\nTroubleshooting:")
    print("  1. Check internet connection")
    print("  2. Try running again (Yahoo Finance can be slow)")
    print("  3. Check if yfinance is installed: pip list | findstr yfinance")