
all: run_uvicorn

.PHONY: requirements
requirements: pyproject.toml
	poetry lock
	poetry install --no-root

.PHONY: migration-generate
migration-generate: requirements
	# generate new revision based on current difference with db
	poetry run alembic revision --autogenerate -m "$(ARGS)"

.PHONY: migrations_generate
migrations_generate: requirements
	poetry run alembic upgrade head

.PHONY: run_uvicorn
run_uvicorn: migrations_generate
	poetry run uvicorn src.main:app --reload
