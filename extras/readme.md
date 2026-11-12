# Extra info
things that shouldn't be deployed with the main chart
- Secrets pre-encrpytion
- LB to expose Chirp UI and Gateway Bridge

```bash
kubectl apply -f chirp_gateway.yaml
kubectl aply -f chirp_lb.yaml
```


Create tls secrets for chirpstack - 
```bash
openssl req -x509 -newkey rsa:2048 \
  -keyout tls.key -out tls.crt \
  -days 3650 -nodes \
  -subj "/CN=chirpstack-basic-station" \
  -addext "subjectAltName=DNS:chirpstack-basic-station.chirp.svc.cluster.local,DNS:chirp.prestonblackburn.com"
```