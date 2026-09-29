"""Ejemplo 8 · El sesgo del zero-shot: la misma pregunta sin el dato y con el dato.

Lección: «El sesgo del zero-shot» y Ejemplos → Ejemplo 6 · El sesgo en código.
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()   # lee TU clave del archivo .env
client = anthropic.Anthropic()

MANUAL = ("El reembolso se abona en un plazo de 10 días hábiles desde la presentación "
          "completa de los documentos.")


def leer_texto(m):
    return "".join(b.text for b in m.content if b.type == "text")


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
