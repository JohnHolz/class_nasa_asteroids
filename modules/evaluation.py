from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import RocCurveDisplay
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import det_curve


def fit_classify(model, x_train, x_test, y_train, y_test):
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    print_2_reports(y_test, y_pred)


def print_2_reports(y_test, y_pred):
    print(classification_report(y_test, y_pred))
    cm = confusion_matrix(y_test, y_pred)
    col = ["N", "Y"]
    print(pd.DataFrame(cm, index=col, columns=col))


def plot_false_negative_rate(y_test, y_prob):
    _, fnr, thresholds = det_curve(y_test, y_prob)
    plt.plot(thresholds, fnr)


def roc_inverse(y_test, y_prob):
    new_prob = list(map(lambda x: 1 - x, y_prob))
    new_test = list(map(lambda x: 1 if x == 0 else 0, y_test.to_numpy()[:, 0]))
    RocCurveDisplay.from_predictions(new_test, new_prob)
