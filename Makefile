
all: run_uvicorn

.PHONY: requirements
requirements: pyproject.toml
	poetry lock
	poetry install --no-root

.PHONY: migration-generate
migration-generate: requirements
	# generate new revision based on current difference with db
	poetry run alembic revision --autogenerate -m "$(ARGS)"

.PHONY: migrations_upgrade
migrations_upgrade: requirements
	poetry run alembic upgrade head

.PHONY: check_flake8
check_flake8: requirements
	poetry run flake8

.PHONY: run_uvicorn
run_uvicorn: migrations_upgrade
	poetry run uvicorn src.main:app --reload
