.PHONY: run dev install format lint test

run:
	uvicorn main:app --reload

dev:
	pip install -r requirements.txt

install:
	python -m venv venv && source venv/bin/activate && make dev

format:
	black .

lint:
	ruff .

test:
	clear
	PYTHONPATH=./ pytest -v --tb=short

check-changelog:
	@echo "🔍 Verificando si CHANGELOG.md fue modificado..."
	@changed_files=$$(git diff --cached --name-only); \
	if echo "$$changed_files" | grep -E '\.py$$|Makefile|^app/|^tests/' > /dev/null; then \
		if ! echo "$$changed_files" | grep -q "CHANGELOG.md"; then \
			echo "❌ ERROR: Se detectaron cambios en el código, pero no se modificó CHANGELOG.md"; \
			echo "👉 Por favor, actualiza CHANGELOG.md antes de hacer commit."; \
			exit 1; \
		fi \
	fi; \
	echo "✅ Verificación de CHANGELOG.md completada con éxito."
