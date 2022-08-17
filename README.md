## Apache Beam RunInferenceAPI example

[Official Example Apache Beam RunInference API pipelines](https://github.com/apache/beam/tree/master/sdks/python/apache_beam/examples/inference) do not provide required files(e.g., input data, model file).
This repository supports making the input file and saving the scikit-lean model. You can quickly try the RunInference API with only one command.

```bash
# Build the enviroment by poetry https://python-poetry.org/docs/#installation
> poetry install
# Make MNIST input dataset and model file, execute RunInferenceAPI with scikit-learn
> make run-sklearn
poetry run python beam_runinferenceapi_sample/mnist.py
INFO:__main__:Save test data as CSV format
INFO:__main__:Start Fiting
INFO:__main__:Save the scikit-learn model as pickle file
INFO:__main__:Start Prediction
Classification report for classifier SVC(gamma=0.001):
              precision    recall  f1-score   support

           0       1.00      0.99      0.99        88
           1       0.99      0.97      0.98        91
           2       0.99      0.99      0.99        86
           3       0.98      0.87      0.92        91
           4       0.99      0.96      0.97        92
           5       0.95      0.97      0.96        91
           6       0.99      0.99      0.99        91
           7       0.96      0.99      0.97        89
           8       0.94      1.00      0.97        88
           9       0.93      0.98      0.95        92

    accuracy                           0.97       899
   macro avg       0.97      0.97      0.97       899
weighted avg       0.97      0.97      0.97       899


poetry run python beam_runinferenceapi_sample/sklearn_mnist_classification.py  --input_file ./data/mnist_data.csv --output ./data/predictions.txt --model_path ./data/mnist_model_svm.pickle
```

> **Note**
> Add PyTorch example which try only one command.
