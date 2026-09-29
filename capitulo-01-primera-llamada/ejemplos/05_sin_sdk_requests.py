"""Ejemplo 5 · Llamar a Claude sin SDK, desde Python, con requests.

Lección: Ejemplos → Ejemplo 2 · Sin SDK, desde Python con requests.
Todo se arma a mano: dirección, cabeceras y cuerpo JSON. Si la API falla un momento, este código no reintenta.
"""
import os

import requests
from dotenv import load_dotenv

load_dotenv()   # lee TU clave del archivo .env

LLAMADA = ("Buenos días, llamo porque me rechazaron el reembolso de una resonancia magnética. "
           "Me dicen que falta la orden médica, pero yo la adjunté.")

respuesta = requests.post(
    "https://api.anthropic.com/v1/messages",
    headers={
        "x-api-key": os.environ["ANTHROPIC_API_KEY"],
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    },
    json={
        "model": "claude-haiku-4-5",
        "max_tokens": 200,
        "messages": [{"role": "user", "content": f"Resume en una frase el motivo de esta llamada: {LLAMADA}"}],
    },
    timeout=60,
)
datos = respuesta.json()
print(datos)                          # la respuesta completa, en JSON
print()
print(datos["content"][0]["text"])    # solo el texto
