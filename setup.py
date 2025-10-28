from setuptools import setup, find_packages

setup(
    name="mlops-pipeline",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "mlflow==2.8.1",
        "prefect==2.14.11", 
        "scikit-learn==1.3.2",
        "pandas==2.1.4",
        "numpy==1.24.3"
    ],
    python_requires=">=3.8"
)