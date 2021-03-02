PY_FILES = `find . \
        -path './.cache' -prune -o \
		-path './docs' -prune -o \
		-path './build' -prune -o \
		-path './scripts' -prune -o \
		-path './.eggs' -prune -o \
		-name '*.py' -print`;

.PHONY: help
.DEFAULT_GOAL := help

##@ Formatters

.PHONY: black isort format

black: ## Python source code formatter
	black --line-length 79 .

isort: ## Python import formatter
	isort --profile black --line-length 79 $(PY_FILES)

format: black isort ## Format all [black, isort]

##@ CI Lint Check

.PHONY: black-ci isort-ci coala-docker coala-podman flake8 pylint pylint-shorter lint

black-ci: ## Check source code formatting
	echo -e "\n# Diff for each file:"; \
	black --line-length 79 --diff .; \
	echo -e "\n# Status:"; \
	black --line-length 79 --check .

isort-ci: ## Check import orders
	isort --profile black --line-length 79 --check-only $(PY_FILES)

flake8: ## Check python source code
	flake8 $(PY_FILES)

pylint: ## Check python source code
	python3 -m pylint $(PY_FILES)

lint: black-ci flake8 pylint isort-ci ## Lint check [black, flake8, pylint, isort-check]

##@ Helpers

.PHONY: help

help: ## Show help message
	@awk 'BEGIN \
          {\
             FS = ":.*##";\
             printf "\nUsage:\n make [OPTION]...\033[36m\033[0m\n" \
          }\
          /^[a-zA-Z_-]+:.*?##/ \
		  {\
		    printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 \
		  }\
		  /^##@/ \
		  { \
            printf "\n\033[1m%s\033[0m\n", substr($$0, 5) \
		  }' \
		  $(MAKEFILE_LIST)
