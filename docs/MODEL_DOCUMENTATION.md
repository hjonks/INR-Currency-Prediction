
# INR Weekly Prediction Model - Documentation

## Model Overview
- **Model Type**: Random Forest Classifier
- **Target**: Predict if INR will weaken (1) or strengthen (0) in next week
- **Accuracy**: 60.34%
- **Training Date**: February 2026
- **Data Period**: 2010-2026 (16 years)

## Input Features (5 required)
1. **MA5** - 5-day moving average of INR/USD
2. **MA20** - 20-day moving average of INR/USD
3. **Lag1** - INR/USD price 1 day ago
4. **Lag3** - INR/USD price 3 days ago
5. **INR_Return** - Today's percentage return

## Usage Instructions

### 1. Load Model
```python
import joblib
model = joblib.load('models/best_weekly_model.pkl')
scaler = joblib.load('models/scaler_weekly.pkl')
```

### 2. Prepare Data
```python
import pandas as pd
data = {
    'MA5': 83.50,
    'MA20': 83.75,
    'Lag1': 83.45,
    'Lag3': 83.60,
    'INR_Return': -0.12
}
df = pd.DataFrame([data])
```

### 3. Scale and Predict
```python
scaled = scaler.transform(df)
prediction = model.predict(scaled)[0]
probability = model.predict_proba(scaled)[0]
```

### 4. Interpret
- **0** = INR will STRENGTHEN next week
- **1** = INR will WEAKEN next week
- **Confidence** = max(probability) * 100

## Performance Metrics
- **Accuracy**: 60.34%
- **Precision (Strengthen)**: 0.47
- **Precision (Weaken)**: 0.86
- **Recall (Strengthen)**: 0.76
- **Recall (Weaken)**: 0.22
- **F1-Score**: 0.73

## Trading Guidelines
- **Confidence ≥ 70%**: Strong signal, consider action
- **Confidence 60-70%**: Moderate signal, use with other indicators
- **Confidence < 60%**: Weak signal, wait for confirmation

## Limitations
- Predicts DIRECTION only, not magnitude
- Based on technical indicators only (no fundamentals)
- Past performance doesn't guarantee future results
- Should be used with other analysis methods
- Model has class imbalance (better at predicting weaken than strengthen)

## Model Parameters
- n_estimators: 100
- max_depth: 3
- min_samples_split: 20
- min_samples_leaf: 10
- random_state: 42

## Project Structure
```
INR_Currency_Project/
├── data/
│   ├── raw/              # Original datasets
│   └── processed/        # Cleaned features
├── models/               # Saved models
├── notebooks/            # Jupyter notebooks
├── docs/                 # Documentation (this file)
└── results/              # Charts and tables
```

## Contact
Dhruv Chaudhary  
Leeds University Business School  
+4407874099010 
February 2026
