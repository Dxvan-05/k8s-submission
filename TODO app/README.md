# To view the app running in k8s

1. Deploy the app to the k8s cluster

```shell
kubectl apply -f manifests/deployment.yaml
```
> [!NOTE]
> The pod should be running after applying the deployment.
> Use ```kubectl get pods```` to get the pod_name

2. Port forward the pod

> [!NOTE]
> Replace <pod_name> with the name of the pod.
> <local_port> to choose the port on your machine where the app will run

```shell
kubectl port-forward <pod_name> <local_port>:6767
```

3. Visit localhost:<local_port> in the browser