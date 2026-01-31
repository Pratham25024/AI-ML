import numpy as np

def weighted_accuracy(y_true, y_pred):
    weights = {0: 1, 1: 2}
    correct_weighted = sum(weights[y] for y, yp in zip(y_true, y_pred) if y == yp)
    total_weighted = sum(weights[y] for y in y_true)
    return correct_weighted / total_weighted
