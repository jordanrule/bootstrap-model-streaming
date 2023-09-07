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

Note that a production deployment could <a href="https://docs.feast.dev/getting-started/concepts/feature-retrieval">utilize SQL</a> for better performance, but for our local deployment we will load the parquet file directly for training and return to our feature store for online inference.

### Train Model

Next we utilize PyTorch to <a href="https://machinelearningmastery.com/lstm-for-time-series-prediction-in-pytorch/">fit a simple LSTM model</a>:

```
pip install torch
pip install matplotlib
wget -O simple_lstm.py https://github.com/jordanrule/bootstrap-online-inference/raw/main/torch/simple_lstm.py
python simple_lstm.py
```

![Weather LSTM](https://github.com/jordanrule/bootstrap-online-inference/raw/main/torch/simple_lstm.png)

```
Epoch 0: train RMSE 6.2340, test RMSE 7.2797
Epoch 10: train RMSE 2.4932, test RMSE 2.4385
Epoch 20: train RMSE 2.4535, test RMSE 2.4168
Epoch 30: train RMSE 2.3856, test RMSE 2.3761
Epoch 40: train RMSE 2.3241, test RMSE 2.3244
```

This is a good model as it generates a comparable RMSE between the train and test dataset, but let's see if we can utilize an attention mechanism to capture elements of the dataset such as seasonality and improve our RMSE.

### Improve Model

We utilize the <a href="https://github.com/Zhenye-Na/DA-RNN/tree/master">DA-RNN</a> model by developed in "A Dual-Stage Attention-Based Recurrent Neural Network for Time Series Prediction" (arXiv preprint arXiv:1704.02971 (2017)) to try to improve on our initial model.

```
wget -O darnn.py https://github.com/jordanrule/bootstrap-online-inference/raw/main/torch/darnn.py
python darnn.py
```

![Weather DA-RNN](https://github.com/jordanrule/bootstrap-online-inference/raw/main/torch/darnn.png)

```
==> Load dataset ...
==> Initialize DA-RNN model ...
==> Use accelerator:  cpu
==> Start training ...
Epochs:  0  Iterations:  197  Loss:  137.73516625438245
Epochs:  1  Iterations:  394  Loss:  52.58221730847044
Epochs:  2  Iterations:  591  Loss:  19.347244980371542
Epochs:  3  Iterations:  788  Loss:  8.870222825386803
Epochs:  4  Iterations:  985  Loss:  4.562742261868443
Epochs:  5  Iterations:  1182  Loss:  4.861971211009824
Epochs:  6  Iterations:  1379  Loss:  2.3649043315255702
Epochs:  7  Iterations:  1576  Loss:  1.5880264813070974
Epochs:  8  Iterations:  1773  Loss:  1.2077774004585247
Epochs:  9  Iterations:  1970  Loss:  1.1395469135817538
Finished Training
```

We have significantly improved on our RMSE, which is a demonstration of how utilizing SOTA models can improve on model accuracy.  We may want to take additional steps to ensure the RMSE numbers are comparable such as ensuring our train/test methodology is entirely consistent, but this model is fine as a prototype.  The next step is to deploy our model in a reproducible manner for online inference. 

## Deploy

### Serve Model

Use <a href="https://mlflow.org/docs/latest/rest-api.html">MLFlow rest api</a> to serve.

### Online Inference

Populate new values in the time series utilizing Feast streaming and note updated model inferences in real-time.

### Monitor Model

Utilize <a href="https://github.com/evidentlyai/evidently/blob/main/examples/integrations/mlflow_logging/historical_drift_visualization.ipynb">Evidently</a> to monitor model drift.
