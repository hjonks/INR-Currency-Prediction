# INR/USD Weekly Direction Prediction
 
**Author:** Dhruv Chaudhary · February 2026

---

## Situation

Currency markets produce continuous streams of price data that are notoriously difficult to forecast. For emerging market currencies like the Indian Rupee, short-term directional moves are driven by a combination of macroeconomic conditions, commodity prices, and global risk sentiment — making them particularly noisy at the daily level. Most retail and academic tools focus on price level forecasting rather than actionable directional signals. This project used 16 years of INR/USD data (2010–2026) to investigate whether a machine learning approach could generate statistically meaningful weekly directional predictions.

## Task

Design and implement a complete machine learning pipeline — from raw data collection through to a saved, deployable model — that predicts whether the Indian Rupee will weaken or strengthen against the USD over the following week. The minimum acceptable accuracy on held-out test data was 56%.

## Action

- Collected 4,160 trading days of INR/USD data alongside commodity prices and macroeconomic indicators via the Yahoo Finance and FRED APIs
- Merged currency, commodity, economic and event data into a single feature set and handled date format inconsistencies across sources
- Engineered features including moving averages (MA5, MA20), lagged prices (Lag1, Lag3) and daily returns; reduced from 35 candidate features to 5 core predictors through Random Forest importance analysis
- Tested 6 model configurations: Logistic Regression, k-NN, Decision Tree, Random Forest, XGBoost and a majority-class baseline — all on a chronological 80/20 split to avoid data leakage
- Identified that predicting weekly direction rather than daily direction significantly reduces signal noise; rebuilt the pipeline around a 5-day forward return target
- Trained a final Random Forest classifier with shallow trees (max_depth=3, min_samples_split=20) to control overfitting on the 3,328 training samples

## Result

- **Final test accuracy: 59.98%** on 832 held-out samples
- Outperformed the best daily model (k-NN, 52.29%) by **+7.69%**
- Exceeded the 56% target
- Training accuracy of 59.16% producing an overfitting gap of just **-0.81%**, demonstrating the model generalises to unseen data
- Weaken class recall of 1.00 — the model reliably identifies weakening periods, which carries the most practical value for downside FX risk management

---

## Model Comparison

| Model | Prediction Target | Test Accuracy |
|---|---|---|
| Baseline (majority class) | Daily | 50.00% |
| Logistic Regression | Daily | 47.83% |
| k-NN | Daily | 52.29% |
| Decision Tree | Daily | 49.03% |
| Random Forest | Daily | 49.03% |
| XGBoost (35 features) | Daily | 47.95% |
| **Random Forest (5 features)** | **Weekly** | **59.98%** |

---

## Final Model

**Algorithm:** Random Forest Classifier  
**Features:** MA5, MA20, Lag1, Lag3, INR_Return  
**Parameters:** n_estimators=100, max_depth=3, min_samples_split=20, min_samples_leaf=10  
**Train/Test split:** 3,328 / 832 (chronological)

**Classification Report:**

| Class | Precision | Recall | F1 |
|---|---|---|---|
| Strengthen | 0.67 | 0.01 | 0.02 |
| Weaken | 0.60 | 1.00 | 0.75 |

---

## Quick Start

```python
import joblib, pandas as pd

model = joblib.load('models/best_weekly_model.pkl')
scaler = joblib.load('models/scaler_weekly.pkl')

features = pd.DataFrame([{
    'MA5': 83.50,
    'MA20': 83.75,
    'Lag1': 83.45,
    'Lag3': 83.60,
    'INR_Return': -0.12
}])

prediction = model.predict(scaler.transform(features))[0]
probability = model.predict_proba(scaler.transform(features))[0]
# prediction: 0 = Strengthen, 1 = Weaken
```

---

## Project Structure

```
INR_Currency_Project/
├── data/
│   ├── raw/                    # currency, commodity, economic, event CSVs
│   └── processed/              # engineered feature sets
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_building.ipynb
│   └── 04_results_visualisations.ipynb
├── models/
│   ├── best_weekly_model.pkl
│   ├── scaler_weekly.pkl
│   └── model_metadata.json
├── scripts/
│   ├── collect_all_data.py
│   └── final_check.py
├── docs/
│   └── MODEL_DOCUMENTATION.md
├── results/
│   ├── figures/
│   └── tables/
└── README.md
```

---

## Stack

Python 3.14 · pandas · numpy · scikit-learn · matplotlib · seaborn · yfinance · fredapi

---

## Contact

**Dhruv Chaudhary** · Leeds University Business School · dhruvdc007@gmail.com
