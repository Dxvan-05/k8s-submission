# Deploying and Accessing on GKE (Ingress)

Prerequisites:
- `gcloud` CLI installed and authenticated
- Billing & Kubernetes Engine API enabled on your GCP project

1. Create the namespace:

```sh
kubectl create namespace exercises
```

2. Create the PostgreSQL secret:

```sh
kubectl create secret generic postgres-secret \
  --from-literal=POSTGRES_PASSWORD=mypassword -n exercises
```

3. Apply database config and statefulset:

```sh
kubectl apply -f manifests/database-configmap.yaml
kubectl apply -f manifests/database.yaml
```

4. Deploy the application and service:

```sh
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service.yaml
```

Note:
- This application is accessed through the Ingress resource in project "Log Output".



