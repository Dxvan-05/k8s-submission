# To view the app running in k8s

1. Deploy the app to the k8s cluster

```shell
kubectl apply -f manifests/deployment.yaml
```

2. Check the logs

```shell
kubectl logs -f deployment/log-app-deployment
```
