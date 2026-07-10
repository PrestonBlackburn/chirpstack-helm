# Extra info
things that shouldn't be deployed with the main chart
- Secrets pre-encrpytion
- LB to expose Chirp UI and Gateway Bridge

```bash
kubectl apply -f chirp_gateway.yaml
kubectl aply -f chirp_lb.yaml
```
