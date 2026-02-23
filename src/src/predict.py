"""
INR Currency Prediction Script
Loads saved model and makes predictions on new data
"""

import joblib
import pandas as pd
import numpy as np
from datetime import datetime

def load_model(model_path='E:/Projects/INR_Currency_Project/models/best_weekly_model.pkl', 
               scaler_path='E:/Projects/INR_Currency_Project/models/scaler_weekly.pkl'):
    """Load the trained model and scaler"""
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    return model, scaler

def prepare_features(ma5, ma20, lag1, lag3, inr_return):
    """Prepare features for prediction"""
    features = {
        'MA5': ma5,
        'MA20': ma20,
        'Lag1': lag1,
        'Lag3': lag3,
        'INR_Return': inr_return
    }
    return pd.DataFrame([features])

def predict_direction(model, scaler, features_df):
    """Make prediction and return result"""
    scaled_features = scaler.transform(features_df)
    prediction = model.predict(scaled_features)[0]
    probability = model.predict_proba(scaled_features)[0]
    
    direction = "WEAKEN" if prediction == 1 else "STRENGTHEN"
    confidence = max(probability) * 100
    
    return {
        'prediction': direction,
        'confidence': confidence,
        'probability_strengthen': probability[0] * 100,
        'probability_weaken': probability[1] * 100
    }

def main():
    """Example usage"""
    # Load model
    model, scaler = load_model()
    
    # Example features
    features = prepare_features(
        ma5=83.50,
        ma20=83.75,
        lag1=83.45,
        lag3=83.60,
        inr_return=-0.12
    )
    
    # Make prediction
    result = predict_direction(model, scaler, features)
    
    # Display result
    print("="*50)
    print("INR WEEKLY PREDICTION")
    print("="*50)
    print(f"Prediction: INR will {result['prediction']}")
    print(f"Confidence: {result['confidence']:.1f}%")
    print(f"\nProbabilities:")
    print(f"  Strengthen: {result['probability_strengthen']:.1f}%")
    print(f"  Weaken: {result['probability_weaken']:.1f}%")
    print("="*50)

if __name__ == "__main__":
    main()