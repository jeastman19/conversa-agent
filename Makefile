# Makefile para conversa-agent

PYTHONPATH=./
APP_MODULE=app.main:app

run:
	clear
	@echo "🚀 Ejecutando conversa-agent con Uvicorn..."
	@PYTHONPATH=$(PYTHONPATH) uvicorn $(APP_MODULE) --reload

test:
	clear
	@echo "🧪 Ejecutando pruebas..."
	@PYTHONPATH=$(PYTHONPATH) pytest -v --maxfail=1 --disable-warnings

lint:
	@echo "🔍 Ejecutando linter..."
	@ruff check .

format:
	@echo "🎨 Formateando código..."
	@ruff format .

install-dev:
	@echo "📦 Instalando dependencias de desarrollo..."
	@pip install -r requirements.txt

clean:
	@echo "🧹 Limpiando archivos temporales..."
	@find . -type d -name "__pycache__" -exec rm -r {} +
	@rm -rf .pytest_cache .mypy_cache

