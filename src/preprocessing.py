import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        
    def preprocess(self, data, target_col, test_size=0.2):
        X = data.drop(columns=[target_col])
        y = data[target_col]
        
        # Handle categorical target
        if y.dtype == 'object':
            y = self.label_encoder.fit_transform(y)
            
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        return train_test_split(X_scaled, y, test_size=test_size, random_state=42)