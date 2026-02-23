from fredapi import Fred

# Test your API key
api_key = '05ce356451567ff503d3eeb085eadb8a'

print("Testing FRED API key...")
print(f"Key: {api_key[:10]}...")

try:
    fred = Fred(api_key=api_key)
    
    # Try to get a simple series
    data = fred.get_series('GDP', observation_start='2020-01-01')
    
    print(f"\n✓ SUCCESS! API key works!")
    print(f"  Downloaded {len(data)} GDP records")
    print(f"\nSample data:")
    print(data.head())
    
except Exception as e:
    print(f"\n✗ ERROR: {e}")
    print("\nPossible issues:")
    print("1. API key is invalid")
    print("2. API key has been revoked")
    print("3. FRED server is down")
    print("\n💡 Solution:")
    print("   Go to: https://fredaccount.stlouisfed.org/apikeys")
    print("   Generate a NEW API key")