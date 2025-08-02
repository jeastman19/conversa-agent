# Guía de contribución al proyecto `conversa-agent`

Este proyecto sigue una arquitectura hexagonal con estructura por módulos funcionales. Toda contribución debe seguir buenas prácticas de desarrollo, diseño limpio y calidad de código.

---

## 📦 Estructura general del proyecto

- El código fuente está en la carpeta `app/`, organizado por módulos funcionales (`chat/`, `rag/`, `classification/`, etc.).
- Cada módulo contiene capas internas: `domain/`, `services/`, `ports/`.
- Los adaptadores externos se ubican en `adapters/` (inbound y outbound).
- El punto de entrada está en `main.py`.

---

## ✅ Reglas generales

- Todos los archivos `.py` deben usar **tipado explícito** (`typing`).
- Los nombres de carpetas, archivos, funciones, variables y clases deben estar en inglés.
- Los archivos de documentación (`README.md`, `CHANGELOG.md`, etc.) deben estar en español.
- Los commits deben estar en español y seguir una descripción clara del cambio realizado.
- Agregar siempre un archivo `__init__.py` en cada carpeta que contenga código Python.

---

## 🧪 Pruebas y testing

- Todos los módulos deben tener tests automatizados en `tests/`.
- El archivo `tests/conftest.py` debe usarse para inicializar implementaciones si se aplica inyección manual (como en `AttentionClassifier`).
- Antes de ejecutar los tests, asegurarse de que `PYTHONPATH=./` esté configurado (esto ya se incluye en el `Makefile`).

### Comando de test:

```bash
make test
```

Esto ejecutará `pytest` con configuración correcta y salida legible.

---

## 🧰 Makefile

Usamos `Makefile` como punto de automatización común. Asegúrate de mantenerlo actualizado si agregás comandos nuevos.

Comandos actuales útiles:

- `make install`: instala dependencias.
- `make run`: ejecuta el servidor de desarrollo (FastAPI).
- `make test`: ejecuta tests con `pytest`.
- `make format`: formatea con `black`.
- `make lint`: ejecuta `ruff`.

---

## 📝 Registro de cambios

Cada vez que se haga un commit que cambie funcionalidad, estructura o pruebas, **debe actualizarse `CHANGELOG.md`**.

Esto es obligatorio y será validado en futuras reglas del `Makefile`.

---

## 🛠️ Estilo y herramientas

- Formateo: `black`
- Linter: `ruff`
- Tests: `pytest`
- Entorno: `venv` + `Makefile`
- Versionado de Python: 3.12+

---

## 🗂️ Archivos ignorados

El proyecto incluye un archivo `.gitignore` configurado para evitar subir archivos sensibles, temporales o locales. Asegúrate de respetarlo y no forzar la inclusión de archivos ignorados.

### Principales exclusiones:

- `.env`, `.env.local`, `.env.dev`: variables sensibles de entorno (usa `.env.example` como plantilla).
- `venv/`: entorno virtual local.
- `__pycache__/`, `.pyc`: archivos de compilación de Python.
- `*.log`, `*.out`: salidas o registros temporales.
- `.vscode/`, `.idea/`: configuraciones del editor.
- `docs/estado_proyecto.json`: archivo de estado interno (no debe compartirse por Git).

Si agregás nuevas herramientas o entornos que generen archivos temporales, recordá incluirlos en el `.gitignore`.

---

## 💬 ¿Preguntas?

Si tienes dudas sobre la arquitectura, estructura de módulos, testing o cualquier decisión técnica, consulta directamente en el canal de desarrollo o con los responsables del proyecto.
