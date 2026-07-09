# Chirp Stack Helm Chart

![Version: 0.0.1](https://img.shields.io/badge/Version-0.0.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.0.1](https://img.shields.io/badge/AppVersion-1.0.0-informational?style=flat-square)



- **chirpstack** — the ChirpStack server itself (official `chirpstack/chirpstack` image)
- **postgresql** — single instance, PVC-backed
- **redis** — single instance, PVC-backed (used for cache/session data only)
- **mosquitto** — MQTT broker ChirpStack uses to talk to gateways
- **gateway-bridge** — ChirpStack Gateway Bridge, translates LR1302
  Semtech UDP `packet_forwarder` protocol into MQTT

**Homepage:** <https://www.chirpstack.io/docs/architecture.html>

## Usage

```bash
helm install -f values.yaml chirp .
```

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| preston | <prestonblckbrn@gmail.com> |  |

## Source Code

* <https://github.com/PrestonBlackburn/chirpstack_helm>

## Dependencies

None


## Requirements

- Sealed Secrets

## Values
 
**TBD**


## Dev

Install deps
```bash
helm dependency update
```

dry run
```bash
helm lint ./chart
helm template ./chart
helm install -f values.yaml chirp . --namespace chirp --dry-run --debug

kubectl create namespace chirp
helm install -f values.yaml chirp . --namespace chirp

# Update helm chart deployment
helm upgrade chirp . -f values.yaml --namespace chirp

helm uninstall chirp --namespace chirp
```

## Verify

```bash
kubectl get pods
kubectl port-forward svc/chirpstack 8080:8080
# open http://localhost:8080  (default login: admin / admin — change immediately)
```
