# Accessing the App

> [!NOTE]
> For this you need to have access to port 80 on the kubernetes loadbalancer.
> This command will forward requests from port 8081 on the local machine to port 80 on the loadbalancer


 1. Create the k3d Cluster

```sh
k3d cluster create -a 2 -p 8081:80@loadbalancer
```

2. Apply persistent storage

```sh
kubectl apply -f ../../manifests/persistent-volume.yaml
```

3. Apply persistent storage claim

```sh
kubectl apply -f ../../manifests/persistent-volume-claim.yaml
```

4. Deploy the TODO app

```sh
kubectl apply -f manifests/deployment.yaml
```


5. Apply the ClusterIP Service for TODO app

```sh
kubectl apply -f manifests/service.yaml
```


6. Apply the Ingress Resource

```sh
kubectl apply -f manifests/ingress.yaml
```



7. Access through browser

Open in your browser:

```
http://localhost:8081
```
