# Bootstrap Model Streaming
Many organizations have a well-defined methodology for offline model inference, processing historical data from a data warehouse with batch processing, but struggle to deploy an appropriate infrastructure and workflow for online model inference via real-time stream processing.  This repository exists to demonstrate a sample online inference workflow utilizing <a href="https://github.com/rabbitmq/rabbitmq-server">RabbitMQ</a> for streaming, <a href="https://github.com/apache/spark">Spark</a> for feature transformation, <a href="https://github.com/feast-dev/feast">Feast</a> for feature serving, and <a href="https://github.com/mlflow/mlflow">MLFlow</a> for model serving, utilizing <a href="https://github.com/kubernetes/kubernetes">Kubernetes</a> for provisioning.  After provisioning, we demonstrate training a simple weather model utilizing <a href="https://github.com/jdb78/pytorch-forecasting">PyTorch</a> and deploying it for real-time inference.

# Provisioning

## Minikube
The first step is to install <a href="https://minikube.sigs.k8s.io/docs/start/">Minikube</a>, note that on some architectures <a href="https://github.com/abiosoft/colima">Colima</a> may be the most straightforward method to run a docker daemon locally.

```
colima start
minikube start
```

## RabbitMQ
Install the <a href="https://www.rabbitmq.com/kubernetes/operator/using-operator.html">RabbitMQ Kubernetes Operator</a>:

```
kubectl apply -f "https://github.com/rabbitmq/cluster-operator/releases/latest/download/cluster-operator.yml"
```
