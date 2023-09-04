# Bootstrap Model Streaming
Many organizations have a well-defined methodology for offline model inference, processing historical data from a data warehouse with batch processing, but struggle to deploy an appropriate infrastructure and workflow for online model inference via real-time stream processing.  This repository exists to demonstrate a sample online inference workflow utilizing <a href="https://github.com/apache/spark">Spark</a> for streaming transformation, <a href="https://github.com/feast-dev/feast">Feast</a> for feature serving, and <a href="https://github.com/mlflow/mlflow">MLFlow</a> for model serving, utilizing <a href="https://github.com/kubernetes/kubernetes">Kubernetes</a> for provisioning.  After provisioning, we demonstrate training a simple weather model utilizing <a href="https://github.com/jdb78/pytorch-forecasting">PyTorch</a> and deploying it for real-time inference.

## Provisioning

### Minikube
The first step is to install <a href="https://minikube.sigs.k8s.io/docs/start/">Minikube</a> and <a href="https://helm.sh/docs/intro/install/">Helm</a>, note that on many architectures <a href="https://github.com/abiosoft/colima">Colima</a> may be the most straightforward method to run a docker daemon locally.

```
colima start
minikube start
```

### Redis

<a href="https://github.com/OT-CONTAINER-KIT/redis-operator">Redis on K8s</a>

### Spark

<a href="https://github.com/GoogleCloudPlatform/spark-on-k8s-operator">Spark on K8s</a>

### Feast

<a href="https://github.com/feast-dev/feast/tree/master/infra/charts/feast">Feast on K8s</a>

## Training

WIP

## Serving

WIP