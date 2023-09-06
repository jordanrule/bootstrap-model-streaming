# Bootstrap Online Inference
This repository illustrates a simple online inference workflow utilizing <a href="https://github.com/feast-dev/feast">Feast</a> for feature serving and <a href="https://github.com/mlflow/mlflow">MLFlow</a> for model serving.  We demonstrate training a simple weather model utilizing <a href="https://github.com/pytorch/pytorch">PyTorch</a> and deploying for real-time inference.

This document is a work in progress.

## Train

### Populate Training Data

Weather data is provided by <a href="https://www.ncei.noaa.gov/cdo-web/datasets">NOAA</a>, a sample dataset for Austin-Bergstrom International Airport is provided.

Create a virtualenv to utilize Feast:
```
python -m venv ~/feast
source ~/feast/bin/activate
```

Install Feast:
```
pip install feast
feast init austin_weather
cd austin_weather/feature_repo
wget -O data/austin_weather.parquet https://github.com/jordanrule/bootstrap-online-inference/raw/main/data/austin_weather.parquet
```

Define the online feature store:

```
TBD
```

### Train Model

Use PyTorch to fit a LSTM model using Feast for online training.

### Validate Model

Use PyTorch on a train/test split to manage bias/variance tradeoff.

## Deploy

### Serve Model

Use <a href="https://mlflow.org/docs/latest/projects.html#project-docker-container-environments">MLFlow</a> to serve.

### Online Inference

Populate new values in the time series utilizing Feast streaming and note updated model inferences in real-time.

### Monitor Model

Utilize <a href="https://github.com/evidentlyai/evidently/blob/main/examples/integrations/mlflow_logging/historical_drift_visualization.ipynb">Evidently</a> to monitor model drift.
