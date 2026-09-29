"""Ejemplo 1 · Cómo llega la clave del archivo .env hasta Anthropic, en cuatro pasos.

Lección: «Dónde se guarda la clave» → Caso 2 · Trabajas en tu computador.
Antes: pon TU clave en el archivo .env de la raíz del repositorio (ver README).
Ejecuta: python capitulo-01-primera-llamada/ejemplos/01_env_cuatro_pasos.py
"""
# 1 · En tu carpeta hay un archivo .env con esta línea:
#     ANTHROPIC_API_KEY=sk-ant-api03-tu-clave-aqui

# 2 · load_dotenv() abre el .env y deja la clave en memoria con el nombre ANTHROPIC_API_KEY
from dotenv import load_dotenv
load_dotenv()

import os
print("Clave cargada:", os.environ["ANTHROPIC_API_KEY"][:12] + "...")   # comprueba, sin mostrarla entera

# 3 · El SDK busca ANTHROPIC_API_KEY en memoria. La clave no aparece escrita en este programa
import anthropic
client = anthropic.Anthropic()

# 4 · La clave viaja cifrada por HTTPS a Anthropic, y vuelve la respuesta
mensaje = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=100,
    messages=[{"role": "user", "content": "Di hola en una frase."}],
)
print(mensaje.content[0].text)
