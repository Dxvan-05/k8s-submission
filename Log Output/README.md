# Accessing the App (GKE NodePort + Ingress)

Prerequisites:
- `gcloud` CLI installed and authenticated and project set
- Billing & Kubernetes Engine API enabled on your GCP project
- `kubectl` configured for the GKE cluster

1. Create a GKE cluster (example):

```sh
gcloud container clusters create ping-pong-cluster \
  --zone=<zone> \
  --num-nodes=3 \
  --disk-size=32 \
  --machine-type=e2-micro
```

2. Get cluster credentials:

```sh
gcloud container clusters get-credentials ping-pong-cluster --zone=<zone>
```

3. Create the exercises namespace:

```sh
kubectl create namespace exercises
```

4. Switch to the exercises namespace:

```sh
kubectl config set-context --current --namespace=exercises
```

5. Apply the ConfigMap:

```sh
kubectl apply -f manifests/configmap.yaml
```

6. Deploy ping-pong-application:

```sh
kubectl apply -f ../ping-pong\ application/manifests/deployment.yaml
```

7. Deploy the log app:

```sh
kubectl apply -f manifests/deployment.yaml
```

8. Apply NodePort Service:

```sh
kubectl apply -f manifests/service.yaml

```

9. Apply the GKE Ingress resource:

```sh
kubectl apply -f manifests/ingress.yaml
```

10. Wait for the Ingress to be provisioned and get its external IP:

```sh
kubectl get ingress -n exercises --watch
# when ADDRESS appears, open in browser:
# http://<INGRESS-EXTERNAL-IP>/
# http://<INGRESS-EXTERNAL-IP>/pingpong
```

