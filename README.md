# End-to-End MLOps Pipeline

Automated ML pipeline using MLflow and Prefect with modular preprocessing and model registry.

## Repository Structure

```
End-to-End-mlops-pipeline/
├── src/
│   ├── __init__.py              # Python package initialization
│   ├── preprocessing.py         # Modular data preprocessing
│   └── model.py                 # ML model with MLflow integration
├── pipeline.py                  # Prefect workflow orchestration
├── run_pipeline.py              # Main runner with MLflow server
├── test_pipeline.py             # Component testing
├── requirements.txt             # Python dependencies
└── README.md                    # Documentation
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Test components (optional)
python test_pipeline.py

# Run full pipeline
python run_pipeline.py
```

## Pipeline Components

### ✅ Modular Preprocessing (`src/preprocessing.py`)
- **StandardScaler**: Feature normalization
- **LabelEncoder**: Categorical target encoding
- **Train/Test Split**: Automated data splitting
- **Reusable Class**: DataPreprocessor for modularity

### ✅ MLflow Integration (`src/model.py`)
- **Experiment Tracking**: Automatic experiment creation
- **Parameter Logging**: Model hyperparameters
- **Metric Logging**: Performance metrics (accuracy)
- **Model Registry**: Automatic model registration
- **Artifact Storage**: Model serialization

### ✅ Prefect Orchestration (`pipeline.py`)
- **Task Decorators**: @task for individual steps
- **Flow Decorator**: @flow for pipeline orchestration
- **Dependency Management**: Automatic task sequencing
- **Error Handling**: Built-in retry and failure handling

### ✅ Model Registry
- **Automatic Registration**: Models registered as "ml_pipeline_model"
- **Version Control**: MLflow handles model versioning
- **Metadata Storage**: Parameters, metrics, and artifacts

## Requirements

### Essential Dependencies
- `mlflow==2.8.1` - Experiment tracking and model registry
- `prefect==2.14.11` - Workflow orchestration
- `scikit-learn==1.3.2` - ML algorithms and preprocessing
- `pandas==2.1.4` - Data manipulation
- `numpy==1.24.3` - Numerical computing

### System Requirements
- Python 3.8+
- 2GB RAM minimum
- Internet connection (for package installation)

## MLflow UI
- **URL**: http://127.0.0.1:5000
- **Access**: Available after running `python run_pipeline.py`
- **Features**: Experiment tracking, model comparison, registry

## Validation Checklist

- [x] **Automated Pipeline**: Prefect orchestrates end-to-end workflow
- [x] **MLflow Integration**: Experiment tracking and model logging
- [x] **Modular Preprocessing**: Reusable DataPreprocessor class
- [x] **Model Registry**: Automatic model registration
- [x] **Minimal Code**: Essential components only
- [x] **Working Example**: Includes sample data generation