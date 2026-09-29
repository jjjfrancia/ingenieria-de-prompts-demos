# Módulo 1 · Plataforma y modelos

Material de práctica de las tres lecciones del módulo. Todo se hace en [claude.ai](https://claude.ai), sin código.
Copia los prompts tal cual; los textos de trabajo están en la carpeta [`materiales/`](materiales/).

| Lección | Qué practicas |
|---|---|
| 1.1 · Cómo funciona Claude: prompt, zero-shot y sesgo | Prompts zero-shot, vago contra preciso, el sesgo y la fecha de corte |
| 1.2 · Por dónde entrar a Claude y qué activar | Tu tabla de decisiones, búsqueda web, Artifacts y memoria |
| 1.3 · Modelos y contexto | Comparar modelos, resumir una conversación larga, reglas en un Project |

---

## Lección 1.1 · Cómo funciona Claude

Abre **una conversación nueva para cada ejercicio**, así uno no influye en el otro.

### Ejercicio 1 · Un zero-shot que funciona

```
Traduce al inglés: Su reembolso fue aprobado y se abonará en cinco días hábiles.
```

¿Hizo falta algún ejemplo? Anota por qué funcionó sin ejemplos.

### Ejercicio 2 · Vago contra preciso

Usa la llamada de [`materiales/llamada_reembolso.txt`](materiales/llamada_reembolso.txt).

Prompt vago, dos veces en dos conversaciones:

```
Resume esta llamada:

[pega aquí la llamada]
```

Prompt preciso, dos veces en dos conversaciones:

```
Resume en una frase de máximo 20 palabras el motivo de esta llamada, sin saludos:

[pega aquí la llamada]
```

Anota el largo de las cuatro respuestas. Los dos prompts son zero-shot: ¿cuál da resultados más parecidos entre sí?

### Ejercicio 3 · Donde el zero-shot no alcanza

En tres conversaciones distintas:

```
Clasifica esta llamada en su categoría de reclamo:

[pega aquí la llamada]
```

Anota las tres categorías. ¿Son las mismas? ¿Son las de tu empresa? Claude no las conoce: las inventa.

### Ejercicio 4 · Encuentra el sesgo

Primero, sin ningún dato:

```
¿Cuánto tarda el reembolso de una consulta médica?
```

Después, en otra conversación, con el párrafo de [`materiales/manual_reembolsos.txt`](materiales/manual_reembolsos.txt):

```
Responde solo con lo que dice este texto. Si la respuesta no está, responde: «No figura en el manual».

<manual>
[pega aquí el párrafo del manual]
</manual>

¿Cuánto tarda el reembolso de una consulta médica?
```

Repite la segunda versión preguntando `¿Cubre la ortodoncia?`. ¿De dónde salió el plazo de la primera respuesta?

### Ejercicio 5 · La fecha de corte

```
¿Qué pasó la semana pasada en el sector salud de mi país?
```

¿Te avisa Claude de que no lo sabe, o responde igual? Repite con la búsqueda web activada y compara.

---

## Lección 1.2 · Por dónde entrar a Claude y qué activar

### Ejercicio 1 · Tu tabla de decisiones

Copia esta tabla y complétala con cinco tareas reales de tu trabajo:

| Tarea | Entrada | Qué activo | Por qué |
|---|---|---|---|
| | | | |

Entradas posibles: chat (web, escritorio o móvil), Claude en Chrome, Claude para Microsoft 365, Cowork, Claude Code.
Funciones posibles: Project, búsqueda web, Research, Artifacts, memoria, connectors, Skills.

### Ejercicio 2 · Con y sin búsqueda

Haz la misma pregunta sobre algo de esta semana, primero sin búsqueda web y después con ella. Mira las fuentes que citó.

### Ejercicio 3 · Un Artifact

```
Convierte mi tabla de decisiones en una tabla limpia, como Artifact, con una columna más:
«riesgo de elegir mal».

[pega aquí tu tabla]
```

Después pide un cambio, por ejemplo «ordénala por riesgo». ¿Qué pasa con el Artifact?

### Ejercicio 4 · Revisa tu memoria

Si tu plan la tiene, abre la configuración de memoria y mira qué recuerda Claude de ti. Decide qué dejarías y qué no.

---

## Lección 1.3 · Modelos y contexto

### Ejercicio 1 · Dos modelos, la misma pregunta

Elige una pregunta difícil de tu trabajo. Hazla con dos modelos distintos del selector de Claude, en dos conversaciones.
Compara la respuesta y el tiempo que tardó cada uno.

### Ejercicio 2 · Resumir y seguir

En una conversación larga que ya tengas:

```
Resume en diez líneas lo que decidimos en esta conversación: los acuerdos, los datos clave
y lo que queda pendiente.
```

Abre un chat nuevo, pega el resumen y sigue trabajando desde ahí.

### Ejercicio 3 · La regla en un Project

Crea un Project de prueba y escribe en sus instrucciones una regla que hoy repites a mano en cada chat, por ejemplo:

```
Responde siempre en tono formal. Nunca prometas plazos: si te preguntan por un plazo,
responde que lo confirma el área responsable.
```

Abre dos chats dentro del Project y comprueba que la regla se cumple en los dos sin repetirla.
