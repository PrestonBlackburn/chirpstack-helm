{{- define "chirpstack.fullname" -}}
{{ .Release.Name }}
{{- end -}}

{{- define "chirpstack.labels" -}}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/part-of: chirpstack
{{- end -}}
