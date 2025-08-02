# Conversa Agent

Agente conversacional modular basado en FastAPI, PostgreSQL y arquitectura hexagonal, diseñado para integrarse fácilmente con canales como Telegram o WhatsApp. Usa RAG para responder preguntas frecuentes y puede extenderse con otras funcionalidades (ERP, catálogos, etc.).

## Estructura del proyecto

```bash
├── app/
│   ├── adapters/        # Interfaces con el mundo externo (Telegram, DB, etc.)
│   ├── application/     # Casos de uso
│   ├── domain/          # Entidades y lógica del dominio
│   ├── infrastructure/  # Implementaciones técnicas (DB, APIs)
│   └── main.py          # Punto de entrada principal
└── tests/
    └── ...              # Tests organizados por módulo
```

## Instalación rápida

```bash
make install
make dev
```

## Ejecutar tests

```bash
make test
```
