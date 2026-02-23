"""
Fix Event Indicators - Proper Date Comparison
"""

import pandas as pd
from datetime import datetime

print("="*70)
print("FIXING EVENT INDICATORS")
print("="*70)

START_DATE = '2010-01-01'
END_DATE = datetime.now().strftime('%Y-%m-%d')

# Create date range
date_range = pd.date_range(start=START_DATE, end=END_DATE, freq='D')

print(f"\nDate range: {date_range[0].date()} to {date_range[-1].date()}")
print(f"Total days: {len(date_range):,}")

# Define events with proper date format
events = {
    'European_Debt_Crisis': (datetime(2011, 1, 1), datetime(2012, 12, 31)),
    'Taper_Tantrum_2013': (datetime(2013, 5, 1), datetime(2013, 12, 31)),
    'Oil_Price_Collapse': (datetime(2014, 6, 1), datetime(2015, 12, 31)),
    'China_Devaluation': (datetime(2015, 8, 1), datetime(2015, 12, 31)),
    'India_Demonetization': (datetime(2016, 11, 8), datetime(2017, 3, 31)),
    'US_China_Trade_War': (datetime(2018, 1, 1), datetime(2019, 12, 31)),
    'EM_Currency_Crisis_2018': (datetime(2018, 4, 1), datetime(2018, 12, 31)),
    'COVID_19_Pandemic': (datetime(2020, 2, 1), datetime(2020, 12, 31)),
    'Oil_War_2020': (datetime(2020, 3, 1), datetime(2020, 4, 30)),
    'Ukraine_Russia_War': (datetime(2022, 2, 24), datetime(2023, 12, 31)),
    'Global_Inflation_Crisis': (datetime(2022, 1, 1), datetime(2023, 12, 31)),
    'Fed_Tightening_Cycle': (datetime(2022, 3, 1), datetime(2023, 12, 31)),
    'Trump_Tariffs_2025': (datetime(2025, 4, 2), datetime(2026, 12, 31)),
    'India_Pakistan_Tensions': (datetime(2025, 5, 1), datetime(2025, 5, 31)),
}

# Create DataFrame with Date column
df_events = pd.DataFrame({'Date': date_range})

print("\nCreating event indicators...\n")

# Add each event column
for event_name, (start_date, end_date) in events.items():
    # Create binary indicator: 1 if date is within event period, 0 otherwise
    df_events[event_name] = df_events['Date'].apply(
        lambda x: 1 if start_date <= x <= end_date else 0
    )
    
    # Count affected days
    event_days = df_events[event_name].sum()
    print(f"  ✓ {event_name}: {event_days} days")

# Add aggregate columns
df_events['Any_Crisis'] = (df_events.drop('Date', axis=1).sum(axis=1) > 0).astype(int)
df_events['Crisis_Count'] = df_events.drop(['Date', 'Any_Crisis'], axis=1).sum(axis=1)

# Set Date as index
df_events.set_index('Date', inplace=True)

# Save
df_events.to_csv('data/raw/event_indicators.csv')

print(f"\n✓ Saved: event_indicators.csv")
print(f"  Shape: {df_events.shape}")
print(f"  Columns: {len(df_events.columns)}")

print(f"\nSummary Statistics:")
print(f"  Total crisis days: {df_events['Any_Crisis'].sum():,}")
print(f"  Normal days: {(df_events['Any_Crisis'] == 0).sum():,}")
print(f"  Crisis percentage: {df_events['Any_Crisis'].mean() * 100:.1f}%")

print(f"\nFirst few rows:")
print(df_events.head(10))

# Show a sample during an event (COVID-19)
print(f"\nSample during COVID-19 (March 2020):")
covid_sample = df_events.loc['2020-03-01':'2020-03-10']
print(covid_sample[['COVID_19_Pandemic', 'Oil_War_2020', 'Any_Crisis', 'Crisis_Count']])

print("\n" + "="*70)
print("✅ DONE! Check the files in Excel now!")
print("="*70)