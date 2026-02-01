# Accessing the App

> [!NOTE]
> For this you need to have access to port 80 on the kubernetes loadbalancer.
> This command will forward requests from port 8081 on the local machine to port 80 on the loadbalancer



 1. Create the k3d Cluster

```sh
k3d cluster create -a 2 -p 8081:80@loadbalancer
```

2. Create the PostgreSQL Secret

```sh
kubectl create secret generic postgres-secret --from-literal=POSTGRES_PASSWORD=mypassword -n exercises
```

3. Apply the Database ConfigMap

```sh
kubectl apply -f manifests/database-configmap.yaml
```

4. Apply the Database StatefulSet

```sh
kubectl apply -f manifests/database.yaml
```

5. Deploy the App

```sh
kubectl apply -f manifests/deployment.yaml
```

6. Apply the ClusterIP Service

```sh
kubectl apply -f manifests/service.yaml
```
> [!NOTE]
> This project share the ingress resource with another project "Log Output"
> Apply the ingress resource from that directory

7. Apply the Ingress Resource

```sh
kubectl apply -f ../Log\ Output/manifests/ingress.yaml
```

8. Access through browser

```
http://localhost:8081/pingpong
```

