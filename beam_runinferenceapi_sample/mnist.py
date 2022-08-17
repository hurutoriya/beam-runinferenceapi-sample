"""
Save scikit-learn model as pickel file and input data for RunInference API under data directory
"""
import csv
import logging
import pickle

import numpy as np
import pandas as pd
from sklearn import datasets, metrics, svm
from sklearn.model_selection import train_test_split

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    digits = datasets.load_digits()

    # Create a classifier: a support vector classifier
    clf = svm.SVC(gamma=0.001)

    # Split data into 50% train and 50% test subsets
    X_train, X_test, y_train, y_test = train_test_split(
        digits.data, digits.target, test_size=0.5, shuffle=False
    )

    logger.info("Save test data as CSV format")
    test_data = [
        np.append(label, data).astype(int) for label, data in zip(y_test, X_test)
    ]
    with open("./data/mnist_data.csv", "w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(test_data)

    logger.info("Start Fiting")
    clf.fit(X_train, y_train)

    logger.info("Save the scikit-learn model as pickle file")
    with open("./data/mnist_model_svm.pickle", "wb") as f:
        pickle.dump(clf, f)

    logger.info("Start Prediction")
    predicted = clf.predict(X_test)

    print(
        f"Classification report for classifier {clf}:\n"
        f"{metrics.classification_report(y_test, predicted)}\n"
    )


if __name__ == "__main__":
    main()
