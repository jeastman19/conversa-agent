
---

### 📄 `CHANGELOG.md`

# Registro de cambios - conversa-agent

## [0.1.1] - 2025-08-01

### Añadido
- Se definió el archivo `.gitignore` incluyendo reglas para `.env`, `.venv/`, y archivos locales.
- Se creó el archivo `CONTRIBUTING.md` con las políticas de colaboración y nombres.
- Se incluyó verificación automática en `Makefile` para asegurar actualización del `CHANGELOG.md`.

### Cambios internos
- Estructura de carpetas con arquitectura hexagonal.
- Preparación para integración con Telegram y RAG.

## [0.1.0] - 2025-08-01

### Añadido
- Estructura base del proyecto con arquitectura hexagonal
- Canal Telegram como primer adapter
- Stub para integración RAG
- Archivo Makefile y requirements.txt
- README.md y .env.example

### Corregido
- Error de tests debido a la falta de inyección de la implementación del clasificador `AttentionClassifier` antes de ejecutar `pytest`.
- Se creó `tests/conftest.py` para importar `basic_rule.py` y asegurar la carga de la implementación concreta antes de los tests.
- Se actualizó el `Makefile` para incluir `PYTHONPATH=./` y configurar `pytest` con salida más clara.
