# To view the app running in k8s

> [!NOTE]
> For this you need to have access to port 30080 on the kubernetes agent node
> This command will forward requests from port 8082 on the local machine to port 30080 on the first agent node of the k8s cluster
> k3d cluster create -a 2 -p 8082:30080@agent:0

1. Deploy the app to the k8s cluster

```shell
kubectl apply -f manifests/deployment.yaml
```


2. Apply NodePort service


```shell
kubectl apply -f manifests/service.yaml
```

3. Visit localhost:8082 in the browser