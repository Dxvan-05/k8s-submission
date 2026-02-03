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
kubectl apply -f ../manifests/persistent-volume.yaml
```



### 3. Apply Persistent Volume Claim

```sh
kubectl apply -f ../manifests/persistent-volume-claim.yaml -n project
```


### 4. Create Namespace Project

```sh
kubectl create namespace project
```


### 5. Switch to Namespace Project

```sh
kubectl config set-context --current --namespace=project
```


### 6. Apply Database ConfigMap

```sh
kubectl apply -f manifests/database-configmap.yaml
```


### 7. Create PostgreSQL Secret

```sh
kubectl create secret generic postgres-secret --from-literal=POSTGRES_PASSWORD=yourpassword
```


### 8. Apply Database

```sh
kubectl apply -f manifests/database.yaml
```


### 9. Deploy Backend

```sh
kubectl apply -f backend/manifests/deployment.yaml
kubectl apply -f backend/manifests/service.yaml
```


### 10. Deploy Frontend

```sh
kubectl apply -f frontend/manifests/deployment.yaml
kubectl apply -f frontend/manifests/service.yaml
```


### 11. Apply the Ingress Resource

```sh
kubectl apply -f manifests/ingress.yaml
```


### 12. Access Through Browser

Open in your browser:

```
http://localhost:8081
```