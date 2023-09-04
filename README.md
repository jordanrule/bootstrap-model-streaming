# Bootstrap Model Streaming
This repository illustrates a simple online inference workflow utilizing <a href="https://github.com/feast-dev/feast">Feast</a> for feature serving and <a href="https://github.com/mlflow/mlflow">MLFlow</a> for model serving.  We demonstrate training a simple weather model utilizing <a href="https://github.com/jdb78/pytorch-forecasting">PyTorch</a> and deploying for real-time inference.

This document is a work in progress.

## Train

### Populate Training Data

Materialize a historical time series in <a href="https://docs.feast.dev/getting-started/quickstart">Feast</a>.

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
