"""
Test FRED API Connection 
"""

import os

# Read API key from file (which is in .gitignore)
def load_api_key():
    """Load FRED API key from api_keys.txt"""
    api_key_file = os.path.join(os.path.dirname(__file__), 'E:Projects/INR_Currency_Project', 'api_keys.txt')
    
    try:
        with open(api_key_file, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    # Assuming format: FRED_API_KEY=your_key_here
                    if 'FRED_API_KEY' in line:
                        return line.split('=')[1].strip()
        raise ValueError("FRED_API_KEY not found in api_keys.txt")
    except FileNotFoundError:
        raise FileNotFoundError("api_keys.txt not found! Create it in project root.")

# Load the API key
FRED_API_KEY = load_api_key()

print(f"✅ API Key loaded: {FRED_API_KEY[:4]}...{FRED_API_KEY[-4:]}")
print("✅ API key loaded securely from api_keys.txt")
