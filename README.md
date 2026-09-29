# Ingeniería de Prompts con Claude — ejemplos del curso

Código de los ejemplos del curso **Ingeniería de Prompts con Claude** de CortexGovernor Academy y DiscoveryFast.
Todo el código está en español y usa un mismo caso: **Andina Salud**, una aseguradora de salud con central de
atención, coordinación clínica, reembolsos y manual de coberturas.

Cada capítulo trae el mismo código en dos formatos:

- un **notebook** (`.ipynb`), para ejecutarlo celda por celda;
- un **script** (`.py`), para ejecutarlo de una vez en tu computador.

## Módulos

| Módulo | Qué practicas | Cómo |
|---|---|---|
| [1 · Plataforma y modelos](modulo-01-plataforma-y-modelos/) | Prompts zero-shot, el sesgo, qué funciones activar, elegir modelo y cuidar el contexto | En claude.ai, sin código: prompts listos para copiar |
| [Código · Tu primera llamada a la API](capitulo-01-primera-llamada/) | API key, llamada sin SDK y con SDK, objeto Message, primera aplicación | [Abrir en Colab](https://colab.research.google.com/github/jjjfrancia/ingenieria-de-prompts-demos/blob/main/capitulo-01-primera-llamada/primera_llamada.ipynb) o en tu computador |

## Lo que necesitas

- Una **API key de Anthropic**. Se crea en [platform.claude.com](https://platform.claude.com/) → API Keys.
  Se muestra una sola vez: guárdala como una contraseña.
- El consumo de los ejemplos es bajo porque usan `claude-haiku-4-5`. Fija un límite de gasto en la consola antes de
  empezar.

## Opción A · En Google Colab (no instalas nada)

1. Pulsa **Abrir** en la tabla de capítulos.
2. En Colab, abre el panel de la llave 🔑 (Secretos), agrega un secreto llamado `ANTHROPIC_API_KEY` con tu clave y
   activa el acceso del notebook.
3. Ejecuta las celdas en orden con ▶ o con `Shift + Enter`.

## Opción B · En tu computador

Necesitas Python 3.10 o superior.

```bash
# 1. Descarga el repositorio
git clone https://github.com/jjjfrancia/ingenieria-de-prompts-demos.git
cd ingenieria-de-prompts-demos

# 2. Crea un entorno virtual e instala las librerías
python -m venv .venv
.venv\Scripts\activate          # en Windows
# source .venv/bin/activate     # en macOS o Linux
pip install -r requirements.txt

# 3. Crea tu archivo .env con la clave
copy .env.example .env          # en Windows
# cp .env.example .env          # en macOS o Linux
```

Abre el archivo `.env` con un editor de texto y reemplaza `sk-ant-api03-tu-clave-aqui` por tu clave. El archivo
`.env` queda solo en tu computador: está en el `.gitignore`, así que git nunca lo sube.

Después puedes ejecutar el capítulo de dos formas:

```bash
# Como script, todo de una vez
python capitulo-01-primera-llamada/primera_llamada.py

# Como notebook, celda por celda
jupyter notebook capitulo-01-primera-llamada/primera_llamada.ipynb
```

También puedes abrir el `.ipynb` en VS Code con la extensión **Jupyter** de Microsoft.

## Sobre la API key

- El archivo `.env` **no cifra** la clave: es texto plano. La protege que nunca salga de tu computador.
- Nunca la escribas en el código, en una celda del notebook ni en un repositorio.
- Si se filtra, revócala en la consola y crea otra.

## Aviso

Claude y Anthropic son marcas registradas de Anthropic PBC. Este repositorio es material de un proveedor de
formación independiente, sin afiliación ni respaldo de Anthropic.
