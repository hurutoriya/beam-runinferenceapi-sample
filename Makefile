# Target source file
SRC=beam_runinferenceapi_sample

.PHONY: lint
lint: ## Run linter
	poetry run flake8 $(SRC)
	poetry run black $(SRC) --check
	poetry run isort $(SRC) --check

.PHONY: fmt
fmt: ## Run formatter
	poetry run black $(SRC)
	poetry run isort $(SRC)

.PHONY: mnist
mnist: ## Save scikit-learn model as pickel file and input data for RunInference API
	poetry run python $(SRC)/mnist.py

.PHONY: run-sklearn
run-sklearn: mnist ## Run RunInferenceAPI in MNIST dataset 
	poetry run python $(SRC)/sklearn_mnist_classification.py  --input_file ./data/mnist_data.csv --output ./data/predictions.txt --model_path ./data/mnist_model_svm.pickle

# ref: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help: ## Generate this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'