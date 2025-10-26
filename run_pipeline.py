#!/usr/bin/env python3
"""
Run the ML pipeline with MLflow tracking server
"""
import subprocess
import sys
import time
from pipeline import ml_pipeline

def start_mlflow_server():
    """Start MLflow tracking server in background"""
    try:
        subprocess.Popen([
            sys.executable, "-m", "mlflow", "server", 
            "--host", "127.0.0.1", "--port", "5000"
        ])
        time.sleep(3)  # Wait for server to start
        print("MLflow server started at http://127.0.0.1:5000")
    except Exception as e:
        print(f"MLflow server may already be running: {e}")

if __name__ == "__main__":
    start_mlflow_server()
    ml_pipeline()