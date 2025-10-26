from prefect import flow, task
import pandas as pd
from src.preprocessing import DataPreprocessor
from src.model import MLModel
from sklearn.datasets import make_classification

@task
def generate_sample_data():
    X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)
    df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(10)])
    df['target'] = y
    return df

@task
def preprocess_data(data):
    preprocessor = DataPreprocessor()
    return preprocessor.preprocess(data, 'target')

@task
def train_model(X_train, X_test, y_train, y_test):
    model = MLModel()
    accuracy = model.train_and_log(X_train, X_test, y_train, y_test)
    return accuracy

@flow(name="ml_pipeline")
def ml_pipeline():
    # Generate or load data
    data = generate_sample_data()
    
    # Preprocess data
    X_train, X_test, y_train, y_test = preprocess_data(data)
    
    # Train and log model
    accuracy = train_model(X_train, X_test, y_train, y_test)
    
    print(f"Pipeline completed with accuracy: {accuracy:.4f}")
    return accuracy

if __name__ == "__main__":
    ml_pipeline()