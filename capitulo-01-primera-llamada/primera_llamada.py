"""Capítulo 1 · Tu primera llamada a Claude — versión script para correr en tu computador.

Mismo código que primera_llamada.ipynb. Antes de ejecutarlo:
  1. pip install -r requirements.txt   (desde la carpeta raíz del repositorio)
  2. copia .env.example como .env y pega tu clave
  3. python capitulo-01-primera-llamada/primera_llamada.py
"""

# ── 1 · Instalar el SDK y cargar tu API key ───────────────────────────────
import os

try:
    from google.colab import userdata          # en Colab: Secretos
    os.environ["ANTHROPIC_API_KEY"] = userdata.get("ANTHROPIC_API_KEY")
    print("Clave cargada desde los Secretos de Colab.")
except ImportError:
    from dotenv import load_dotenv             # en tu computador: archivo .env
    load_dotenv()
    print("Clave cargada desde el archivo .env.")

assert os.environ.get("ANTHROPIC_API_KEY"), "No encontré ANTHROPIC_API_KEY. Revisa el paso anterior."

# ── 2 · Sin SDK: la petición web armada a mano ────────────────────────────
import requests

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

# ── 3 · Con el SDK: la misma llamada ──────────────────────────────────────
import anthropic

client = anthropic.Anthropic()        # lee ANTHROPIC_API_KEY del entorno

mensaje = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=200,
    messages=[{"role": "user", "content": f"Resume en una frase el motivo de esta llamada: {LLAMADA}"}],
)

print(mensaje)                        # el objeto Message entero

# ── Leer la respuesta en un solo lugar ────────────────────────────────────
def leer_texto(mensaje):
    """Junta el texto de todos los bloques de tipo text."""
    return "".join(bloque.text for bloque in mensaje.content if bloque.type == "text")


print("Texto:      ", leer_texto(mensaje))
print("stop_reason:", mensaje.stop_reason)
print("tokens:     ", mensaje.usage.input_tokens, "de entrada +", mensaje.usage.output_tokens, "de salida")
print("id:         ", mensaje.id)

# ── 4 · Zero-shot vago y zero-shot preciso ────────────────────────────────
VAGO = "Resume esta llamada:"
PRECISO = "Resume en una frase de máximo 20 palabras el motivo de esta llamada, sin saludos:"

for nombre, instruccion in [("vago", VAGO), ("preciso", PRECISO)]:
    for intento in range(3):
        m = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=300,
            messages=[{"role": "user", "content": f"{instruccion}\n\n{LLAMADA}"}],
        )
        texto = leer_texto(m)
        print(f"{nombre} #{intento + 1}: {len(texto.split())} palabras -> {texto[:90]}")

# ── 5 · El sesgo del zero-shot ────────────────────────────────────────────
MANUAL = ("El reembolso se abona en un plazo de 10 días hábiles desde la presentación "
          "completa de los documentos.")


def preguntar(pregunta, con_manual):
    if con_manual:
        prompt = ("Responde solo con lo que dice el manual. Si no está, responde: No figura en el manual.\n"
                  f"<manual>{MANUAL}</manual>\n{pregunta}")
    else:
        prompt = pregunta
    m = client.messages.create(model="claude-haiku-4-5", max_tokens=200,
                               messages=[{"role": "user", "content": prompt}])
    return leer_texto(m)


for pregunta in ["¿Cuánto tarda el reembolso de una consulta médica?", "¿Cubre la ortodoncia?"]:
    print("PREGUNTA:", pregunta)
    print("  sin manual:", preguntar(pregunta, False))
    print("  con manual:", preguntar(pregunta, True))
    print()

# ── 6 · Del prompt a una aplicación ───────────────────────────────────────
INSTRUCCION = "Resume en una frase de máximo 25 palabras el motivo de esta llamada, sin saludos:"


def resumir_llamada(transcripcion, max_tokens=150):
    mensaje = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": f"{INSTRUCCION}\n\n{transcripcion}"}],
    )
    resultado = {
        "resumen": leer_texto(mensaje),
        "completo": mensaje.stop_reason == "end_turn",
        "tokens_entrada": mensaje.usage.input_tokens,
        "tokens_salida": mensaje.usage.output_tokens,
        "id": mensaje.id,
    }
    if mensaje.stop_reason == "max_tokens":
        resultado["alerta"] = "El resumen se cortó: revisarlo a mano o subir max_tokens."
    return resultado


try:
    for tope in (150, 5):                     # con 5 tokens el resumen se corta a propósito
        r = resumir_llamada(LLAMADA, max_tokens=tope)
        if r["completo"]:
            print(f"max_tokens={tope} -> Resumen:", r["resumen"])
        else:
            print(f"max_tokens={tope} -> Revisar:", r["alerta"], "| texto cortado:", r["resumen"])
        print("   tokens:", r["tokens_entrada"], "+", r["tokens_salida"], "· id:", r["id"])
except anthropic.AuthenticationError:
    print("La API key no es válida: revisa el paso 1.")
except anthropic.RateLimitError:
    print("La API está saturada después de los reintentos: espera un momento y vuelve a ejecutar.")
