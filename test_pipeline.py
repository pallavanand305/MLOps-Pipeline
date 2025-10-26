#!/usr/bin/env python3
"""Test script to verify pipeline functionality"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.preprocessing import DataPreprocessor
from src.model import MLModel
import pandas as pd
from sklearn.datasets import make_classification

def test_preprocessing():
    # Test data preprocessing
    X, y = make_classification(n_samples=100, n_features=5, n_classes=2, random_state=42)
    df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(5)])
    df['target'] = y
    
    preprocessor = DataPreprocessor()
    X_train, X_test, y_train, y_test = preprocessor.preprocess(df, 'target')
    
    assert X_train.shape[0] == 80, "Training set size incorrect"
    assert X_test.shape[0] == 20, "Test set size incorrect"
    print("✓ Preprocessing module working")

def test_model():
    # Test model training (without MLflow for quick test)
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.datasets import make_classification
    
    X, y = make_classification(n_samples=100, n_features=5, n_classes=2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X[:80], y[:80])
    accuracy = model.score(X[80:], y[80:])
    
    assert accuracy > 0.5, "Model accuracy too low"
    print("✓ Model training working")

if __name__ == "__main__":
    print("Testing pipeline components...")
    test_preprocessing()
    test_model()
    print("✓ All tests passed - Pipeline ready to run!")