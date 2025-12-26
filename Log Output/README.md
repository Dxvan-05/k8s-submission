# Accessing the App

> [!NOTE]
> For this you need to have access to port 80 on the kubernetes loadbalancer.
> This command will forward requests from port 8081 on the local machine to port 80 on the loadbalancer


 1. Create the k3d Cluster

```sh
k3d cluster create -a 2 -p 8081:80@loadbalancer
```


2. Deploy the App

```sh
kubectl apply -f manifests/deployment.yaml
```


3. Apply the ClusterIP Service

```sh
kubectl apply -f manifests/service.yaml
```


4. Apply the Ingress Resource

```sh
kubectl apply -f manifests/ingress.yaml
```

This routes traffic from the loadbalancer to service.


5. Access through browser

Open in your browser:

```
http://localhost:8081
```
