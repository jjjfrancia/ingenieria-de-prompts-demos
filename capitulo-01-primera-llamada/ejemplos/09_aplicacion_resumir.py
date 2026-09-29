"""Ejemplo 9 · Del prompt zero-shot a una aplicación que decide según el objeto Message.

Lección: «Del prompt zero-shot a una aplicación que usa el objeto Message».
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()   # lee TU clave del archivo .env
client = anthropic.Anthropic()

INSTRUCCION = "Resume en una frase de máximo 25 palabras el motivo de esta llamada, sin saludos:"
LLAMADA = ("Buenos días, llamo porque me rechazaron el reembolso de una resonancia magnética. "
           "Me dicen que falta la orden médica, pero yo la adjunté.")


def leer_texto(m):
    return "".join(b.text for b in m.content if b.type == "text")


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
    print("La API key no es válida: revisa tu archivo .env.")
except anthropic.RateLimitError:
    print("API saturada después de los reintentos: espera un momento y vuelve a ejecutar.")
