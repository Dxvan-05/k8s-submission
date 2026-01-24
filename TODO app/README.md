## Accessing the App

> [!NOTE]
> You must have access to port **80** on the Kubernetes load balancer.
> This setup forwards requests from **localhost:8081** to **port 80** on the load balancer.

---

### 1. Create the k3d Cluster

```sh
k3d cluster create -a 2 -p 8081:80@loadbalancer
```



### 2. Apply Persistent Storage

```sh
kubectl apply -f ../../manifests/persistent-volume.yaml
```



### 3. Apply Persistent Volume Claim

```sh
kubectl apply -f ../../manifests/persistent-volume-claim.yaml
```


### 4. Deploy Backend

```sh
kubectl apply -f backend/manifests/deployment.yaml
kubectl apply -f backend/manifests/service.yaml
```


### 5. Deploy Frontend

```sh
kubectl apply -f frontend/manifests/deployment.yaml
kubectl apply -f frontend/manifests/service.yaml
```


### 6. Apply the Ingress Resource

```sh
kubectl apply -f manifests/ingress.yaml
```


### 7. Access Through Browser

Open in your browser:

```
http://localhost:8081
```