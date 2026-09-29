# Capítulo 1 · Tu primera llamada a Claude

Todos los ejemplos de la lección **«Primeros pasos: API key y primera llamada»**, cada uno en su propio archivo.

## Antes de empezar: pon TU clave

Cada ejemplo usa tu propia API key de Anthropic. Nunca se escribe dentro del código.

- **En Colab:** panel de la llave 🔑 → «Agregar un secreto» → Nombre `ANTHROPIC_API_KEY`, Valor tu clave →
  activa «Acceso del notebook». Después ejecuta el contenido de `ejemplos/02_colab_secretos.py` en la primera celda.
- **En tu computador:** en la carpeta raíz del repositorio, copia `.env.example` como `.env`, ábrelo con el Bloc de
  notas y reemplaza `sk-ant-api03-tu-clave-aqui` por tu clave. El `.env` no se sube a GitHub porque está en el
  `.gitignore`.

## Los ejemplos, en el orden de la lección

| Archivo | Qué muestra | Parte de la lección |
|---|---|---|
| `ejemplos/01_env_cuatro_pasos.py` | Cómo llega la clave del `.env` hasta Anthropic, en cuatro pasos | Dónde se guarda la clave → Caso 2 |
| `ejemplos/02_colab_secretos.py` | Cargar la clave desde los Secretos de Colab | Dónde se guarda la clave → Caso 1 |
| `ejemplos/03_keyring_cifrada.py` | Guardar la clave cifrada en el sistema operativo | Si quieres que la clave quede cifrada de verdad |
| `ejemplos/04_sin_sdk_curl.sh` | Llamar a Claude sin SDK, desde la terminal | Ejemplo 1 · Sin SDK, con curl |
| `ejemplos/05_sin_sdk_requests.py` | Llamar a Claude sin SDK, desde Python | Ejemplo 2 · Sin SDK, con requests |
| `ejemplos/06_con_sdk_message.py` | La misma llamada con el SDK y leer el objeto Message | Ejemplos 3 y 4 |
| `ejemplos/07_zero_shot_vago_preciso.py` | Un zero-shot vago y uno preciso, tres veces cada uno | Ejemplo 5 · El zero-shot cambia de forma |
| `ejemplos/08_sesgo.py` | La misma pregunta sin el dato y con el dato | El sesgo del zero-shot |
| `ejemplos/09_aplicacion_resumir.py` | El prompt convertido en una aplicación | Del prompt zero-shot a una aplicación |
| `primera_llamada.ipynb` | Todo lo anterior en un solo notebook, para Colab | Práctica |

## Cómo ejecutar un ejemplo

Desde la carpeta raíz del repositorio:

```bash
python capitulo-01-primera-llamada/ejemplos/06_con_sdk_message.py
```

En Colab, abre `primera_llamada.ipynb` con el botón del README principal y ejecuta las celdas en orden.

## Ejercicios

1. **Ejecútalo tal cual** con tu clave y lee la salida.
2. **Cámbialo:** reemplaza la llamada de Andina Salud por una tuya y vuelve a ejecutar.
3. **Compáralo:** ejecuta dos veces el mismo ejemplo y anota qué cambia en la respuesta y qué no.

Las respuestas de Claude cambian en cada ejecución: la tuya no será idéntica a la de tus compañeros.
