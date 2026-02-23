"""
Final Data Collection Verification
Check all 4 required CSV files
"""

import pandas as pd
import os

print("="*70)
print("FINAL DATA VERIFICATION")
print("="*70)

files = [
    'currency_data.csv',
    'economic_indicators.csv',
    'commodity_prices.csv',
    'event_indicators.csv'
]

all_good = True

for filename in files:
    filepath = f'data/raw/{filename}'
    print(f"\n📄 {filename}")
    
    if os.path.exists(filepath):
        try:
            df = pd.read_csv(filepath, index_col=0, parse_dates=True)
            
            file_size = os.path.getsize(filepath) / 1024  # KB
            
            print(f"  ✓ File exists ({file_size:.1f} KB)")
            print(f"  ✓ Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
            print(f"  ✓ Date range: {df.index[0].date()} to {df.index[-1].date()}")
            
            # Show columns
            cols_str = ', '.join(df.columns[:3].tolist())
            if len(df.columns) > 3:
                cols_str += f", ... (+{len(df.columns)-3} more)"
            print(f"  ✓ Columns: {cols_str}")
            
            # Check for data
            total_values = df.notna().sum().sum()
            print(f"  ✓ Non-null values: {total_values:,}")
            
        except Exception as e:
            print(f"  ✗ Error reading file: {e}")
            all_good = False
    else:
        print(f"  ✗ FILE NOT FOUND!")
        all_good = False

print("\n" + "="*70)

if all_good:
    print("✅ ALL FILES VERIFIED!")
    print("="*70)
    print("\n🎉 WEEK 1 COMPLETE!")
    print("\n📋 Next Steps:")
    print("  1. Open files in Excel to visually inspect")
    print("  2. Start Week 2 - Exploratory Data Analysis")
    print("  3. Create Jupyter notebooks")
    print("  4. Make visualizations")
else:
    print("❌ SOME FILES MISSING OR CORRUPTED")
    print("="*70)
    print("\n🔧 Run these scripts to fix:")
    print("  - python scripts/simple_economic_yahoo.py")
    print("  - python scripts/fix_event_indicators.py")

print("\n" + "="*70)