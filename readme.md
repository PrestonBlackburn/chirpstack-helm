
# Helm for ChirpStack LoRaWAN Gateway


## Pointing your LR1302 gateway at this instead of TTN

On the gateway, find `global_conf.json` or `local_conf.json` for
`packet_forwarder` and update the `gateway_conf` section:

```json
"gateway_conf": {
  "server_address": "<IP of a k8s node>",
  "serv_port_up": 1700,
  "serv_port_down": 1700
}
```

By default (`gatewayBridge.hostNetwork: true`), the Gateway Bridge binds
directly to port 1700 on whichever node its pod lands on — so
`server_address` just needs to be that node's IP, no other networking setup
required. If you'd rather not rely on a specific node (e.g. multi-node
cluster where the pod could move), set `gatewayBridge.hostNetwork: false`
and use the NodePort service instead (default `31700` — you'd then set
`serv_port_up`/`serv_port_down` to `31700` on the gateway).

## Before you install

1. **Region config.** `files/region_us915_1.toml` (US915 sub-band/FSB2,
   fetched from the ChirpStack repo) is included and set as the default in
   `values.yaml` (`chirpstack.region: us915_1`) since that's TTN's default
   US frequency plan. **This must match the 8-channel sub-band already
   programmed into your LR1302's channel plan** — check its
   `global_conf.json`/`local_conf.json` channel frequencies if you're not
   sure it's FSB2. If it's a different sub-band, grab the matching
   `region_us915_N.toml` from:
   https://github.com/chirpstack/chirpstack/tree/master/chirpstack/configuration
   drop it in `files/`, remove `region_us915_1.toml`, and update
   `chirpstack.region` to match.


2. **Sealed Secrets** (optional - requires sealed secrets to be installed on your cluster)   
Create the sealed secret -   
Test a secret  
```bash
# Seal the secret
kubeseal --format yaml < extras/plain_secret.yaml > chart/templates/chirp-secrets.yaml --controller-name=sealed-secrets --controller-namespace=sealed-secrets

# Apply the sealed secret
kubectl apply -f example-sealed-secret.yaml

# Verify the secret was created
kubectl get secret my-secret -n default
```