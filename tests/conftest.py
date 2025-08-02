# Este archivo se ejecuta automáticamente al iniciar pytest
# Forzamos la carga de la implementación real del clasificador

from app.classification.services import basic_rule  # noqa: F401
