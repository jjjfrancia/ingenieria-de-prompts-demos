#!/usr/bin/env bash
# Ejemplo 4 · Llamar a Claude sin SDK, desde la terminal, con curl.
# Lección: Ejemplos → Ejemplo 1 · Sin SDK, desde la terminal con curl.
# Antes, pon TU clave en la terminal:   export ANTHROPIC_API_KEY=sk-ant-api03-tu-clave
# En Windows, ejecútalo desde Git Bash:  bash 04_sin_sdk_curl.sh
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-haiku-4-5",
    "max_tokens": 200,
    "messages": [
      {
        "role": "user",
        "content": "Resume en una frase el motivo de esta llamada: Buenos días, llamo porque me rechazaron el reembolso de una resonancia magnética. Me dicen que falta la orden médica, pero yo la adjunté."
      }
    ]
  }'
