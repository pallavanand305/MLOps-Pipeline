import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

class MLModel:
    def __init__(self, experiment_name="ml_pipeline"):
        mlflow.set_experiment(experiment_name)
        self.model = RandomForestClassifier(random_state=42)
        
    def train_and_log(self, X_train, X_test, y_train, y_test):
        with mlflow.start_run():
            # Train model
            self.model.fit(X_train, y_train)
            
            # Predictions and metrics
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            
            # Log parameters and metrics
            mlflow.log_params(self.model.get_params())
            mlflow.log_metric("accuracy", accuracy)
            
            # Log model
            mlflow.sklearn.log_model(
                self.model, 
                "model",
                registered_model_name="ml_pipeline_model"
            )
            
            return accuracy