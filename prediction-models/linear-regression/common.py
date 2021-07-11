import numpy as np
import pandas as pd

# Normalize data - minmax approach
def normalize_data(data):
    data = (data-data.min())/(data.max()-data.min())
    return data.values.tolist()

# Reverse normalizaton
def feature_normalization(data, min, max):
    return (data-min)/(max-min)

# Reverse normalizaton
def reverse_normalization(norm_data, min, max):
    return norm_data*(max - min) + min    

# Find the minimum and maximum for each column
def dataset_minmax(dataset):
	return dataset.min(), dataset.max()

# Load a CSV file
def load_csv(url):
    print('Load data')
    return pd.read_csv(url)

def input_output_split(data):
    X = []
    Y = []
    for item in data:
        x1 = item[0]
        x2 = item[1]
        x3 = item[3]
        y = item[2]
        arr = [x1, x2, x3]
        X.append(arr)
        Y.append(y)
    X = np.array(X)
    Y = np.array(Y)
    return X, Y

def mean_square_error(y_test, predicted):
    error = 0
    for i in range(len(y_test)):
        error += (y_test[i] - predicted[i]) ** 2
    return error / len(y_test)