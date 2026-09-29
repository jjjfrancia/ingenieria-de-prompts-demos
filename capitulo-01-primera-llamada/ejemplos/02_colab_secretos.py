"""Ejemplo 2 · Cargar TU clave desde los Secretos de Colab.

Lección: «Dónde se guarda la clave» → Caso 1 · Trabajas en Google Colab.
Solo funciona dentro de Google Colab: pega estas líneas en la primera celda del notebook.
Antes: panel de la llave 🔑 → «Agregar un secreto» → Nombre ANTHROPIC_API_KEY, Valor tu clave →
activa «Acceso del notebook».
"""
import os
from google.colab import userdata

os.environ["ANTHROPIC_API_KEY"] = userdata.get("ANTHROPIC_API_KEY")
print("Clave cargada desde los Secretos de Colab:", os.environ["ANTHROPIC_API_KEY"][:12] + "...")
