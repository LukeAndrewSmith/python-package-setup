import numpy as np
from preprocessing.get_data import get_data


def calculate_mean():
    return np.mean(get_data())
