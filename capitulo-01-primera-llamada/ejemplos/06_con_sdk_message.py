"""Ejemplo 6 · La misma llamada con el SDK, y leer el objeto Message en un solo lugar.

Lección: Ejemplos → Ejemplo 3 · Con el SDK, y Ejemplo 4 · Lo que sale mal.
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()   # lee TU clave del archivo .env
client = anthropic.Anthropic()

LLAMADA = ("Buenos días, llamo porque me rechazaron el reembolso de una resonancia magnética. "
           "Me dicen que falta la orden médica, pero yo la adjunté.")


def leer_texto(mensaje):
    """Junta el texto de todos los bloques de tipo text. El resto del programa solo usa esta función."""
    return "".join(bloque.text for bloque in mensaje.content if bloque.type == "text")


mensaje = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=200,
    messages=[{"role": "user", "content": f"Resume en una frase el motivo de esta llamada: {LLAMADA}"}],
)

# Lo que sale mal: el objeto Message no tiene .text -> AttributeError. Quita el # para verlo.
# print(mensaje.text)

print("Texto:      ", leer_texto(mensaje))
print("stop_reason:", mensaje.stop_reason)
print("usage:      ", mensaje.usage.input_tokens, "+", mensaje.usage.output_tokens, "tokens")
print("id:         ", mensaje.id)
