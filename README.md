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

Define the feature store:

```
wget -O weather_repo.py https://github.com/jordanrule/bootstrap-online-inference/raw/main/feast/weather_repo.py
feast materialize 2020-01-01T00:00:00 2023-01-01T00:00:00
feast apply
```

A sample query from our feature store is defined below:

```
store = FeatureStore(repo_path=".")
feature_service = store.get_feature_service("weather_stats_online")
entity_df = pd.DataFrame.from_dict(
    {
        "location": [
        	'Austin', 
        	'Austin', 
        	'Austin',
        ],
        "event_timestamp": [
            datetime(2021, 4, 12, 10, 59, 42),
            datetime(2021, 4, 12, 8, 12, 10),
            datetime(2021, 4, 12, 16, 40, 26),
        ],
    }
)
features = store.get_historical_features(
    features=feature_service, 
    entity_df=entity_df,
)
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
