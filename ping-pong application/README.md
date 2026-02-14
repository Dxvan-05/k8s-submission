# Deploying and Accessing on GKE (LoadBalancer)

Prerequisites:
- `gcloud` CLI installed and authenticated
- Billing & Kubernetes Engine API enabled on your GCP project

1. Create a GKE cluster (example):

```sh
gcloud container clusters create ping-pong-cluster \
  --zone=<zone> \
  --num-nodes=3 \
  --disk-size=32 \
  --machine-type=e2-micro
```

2. Get cluster credentials for `kubectl`:

```sh
gcloud container clusters get-credentials ping-pong-cluster --zone=<zone>
```

3. Create the namespace:

```sh
kubectl create namespace exercises
```

4. Create the PostgreSQL secret:

```sh
kubectl create secret generic postgres-secret \
  --from-literal=POSTGRES_PASSWORD=mypassword -n exercises
```

5. Apply database config and statefulset:

```sh
kubectl apply -f manifests/database-configmap.yaml
kubectl apply -f manifests/database.yaml
```

6. Deploy the application and service:

```sh
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service.yaml
```

7. Wait for the external IP to be provisioned and get it:

```sh
# Watch status
kubectl get svc -n exercises --watch
```

8. Access the app through the LoadBalancer IP (service port is `1234`):

```sh
# replace <EXTERNAL-IP> with the value returned above
curl "http://<EXTERNAL-IP>:1234/pingpong"

# or open in a browser:
http://<EXTERNAL-IP>:1234/pingpong
```

