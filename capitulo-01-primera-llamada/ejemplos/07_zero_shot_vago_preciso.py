"""Ejemplo 7 · El zero-shot cambia de forma: un prompt vago y uno preciso, tres veces cada uno.

Lección: Ejemplos → Ejemplo 5 · El zero-shot cambia de forma.
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()   # lee TU clave del archivo .env
client = anthropic.Anthropic()

LLAMADA = ("Buenos días, llamo porque me rechazaron el reembolso de una resonancia magnética. "
           "Me dicen que falta la orden médica, pero yo la adjunté.")
VAGO = "Resume esta llamada:"
PRECISO = "Resume en una frase de máximo 20 palabras el motivo de esta llamada, sin saludos:"


def leer_texto(m):
    return "".join(b.text for b in m.content if b.type == "text")


for nombre, instruccion in [("vago", VAGO), ("preciso", PRECISO)]:
    for intento in range(3):
        m = client.messages.create(model="claude-haiku-4-5", max_tokens=300,
                                   messages=[{"role": "user", "content": f"{instruccion}\n\n{LLAMADA}"}])
        texto = leer_texto(m)
        print(f"{nombre} #{intento + 1}: {len(texto.split())} palabras -> {texto[:90]}")
