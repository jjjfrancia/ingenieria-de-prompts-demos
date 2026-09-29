"""Ejemplo 3 · Guardar TU clave cifrada en el almacén del sistema operativo.

Lección: «Si quieres que la clave quede cifrada de verdad».
El .env es texto plano. Con keyring, la clave queda cifrada en el Administrador de credenciales de Windows
o en el Llavero de macOS.

Instala:                         pip install keyring
Guarda tu clave, una sola vez:   python 03_keyring_cifrada.py guardar sk-ant-api03-tu-clave
Úsala:                           python 03_keyring_cifrada.py
"""
import sys

import anthropic
import keyring

SERVICIO, USUARIO = "anthropic", "api_key"

if len(sys.argv) == 3 and sys.argv[1] == "guardar":
    keyring.set_password(SERVICIO, USUARIO, sys.argv[2])
    print("Clave guardada cifrada en el almacén del sistema operativo.")
    sys.exit(0)

clave = keyring.get_password(SERVICIO, USUARIO)
if not clave:
    sys.exit("No hay clave guardada. Ejecuta primero: python 03_keyring_cifrada.py guardar TU-CLAVE")

client = anthropic.Anthropic(api_key=clave)
m = client.messages.create(model="claude-haiku-4-5", max_tokens=100,
                           messages=[{"role": "user", "content": "Di hola en una frase."}])
print(m.content[0].text)
