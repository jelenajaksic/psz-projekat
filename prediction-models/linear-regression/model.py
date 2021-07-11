import numpy as np
import pandas as pd
from random import randrange
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000, batch_size=64, regularization_coeff = 0.001):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.batch_size = batch_size
        self.weights, self.bias = None, None
        self.regularization_coeff = regularization_coeff
        
    @staticmethod
    def _mean_squared_error(y, y_hat):
        error = 0
        for i in range(len(y)):
            error += (y[i] - y_hat[i]) ** 2
        return error / len(y)
    
    def fit(self, X, y):
        # 1. Initialize weights and bias to zeros
        self.weights = np.zeros(X.shape[1])
        self.bias = 0
        
        # 2. Perform gradient descent
        print('Perform gradient descent')
        for i in range(self.n_iterations):
            batch = 1
            while batch*self.batch_size < X.shape[0]:
                X_batch = X[((batch-1)*self.batch_size):(batch*self.batch_size), :]
                y_batch = y[((batch-1)*self.batch_size):(batch*self.batch_size)]
                # Line equation
                y_hat = np.dot(X_batch, self.weights) + self.bias
                
                # Calculate derivatives
                partial_w = (1 / X_batch.shape[0]) * (np.dot(X_batch.T, (y_hat - y_batch)))
                partial_d = (1 / X_batch.shape[0]) * (np.sum(y_hat - y_batch))

                # L2 Regularization function
                reg = (self.regularization_coeff/ X_batch.shape[0]) * self.weights
                
                # Update the coefficients
                self.weights -= self.learning_rate * partial_w + reg
                self.bias -= self.learning_rate * partial_d

                batch += 1       
        
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

# Normalize data - minmax approach
def normalize_data(data):
    data = (data-data.min())/(data.max()-data.min())
    return data.values.tolist()

# Reverse normalization
def rev_normalization(data_norm, data_min, data_max):
	return data_norm*(data_max-data_min) + data_min

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
        x3 = item[2]
        x4 = item[5]
        x5 = item[6]
        x6 = item[7]
        y = item[4]
        arr = [x1, x2, x3, x4, x5, x6]
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

# Train model
def model_predict (X_train, X_test, y_train, y_test, l_rate=0.01, r_coeff=0.01, n_iter=1000, b_size=64):
    print('model_predict')
    model = LinearRegression(learning_rate=l_rate, regularization_coeff=r_coeff, n_iterations=n_iter, batch_size=b_size)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    error = model._mean_squared_error(y_test, preds)
    return model.bias, model.weights, error

# Split a dataset into a train and test set
def train_test_split(data, split):
    print('train_test_split')
    data_train = list()
    data_test = list(data)
    train_size = split * len(data)
    while len(data_train) < train_size:
        index = randrange(len(data_test))
        data_train.append(data_test.pop(index))
    return data_train, data_test

# Choose hyperparameters
def choose_hyperparameters (X_train, y_train, X_test, y_test):
    print('choose_hyperparameters')
    bias_list = list()
    weights_list = list()
    errors = list()
    hyperparameters = list()
    for lr in [0.1, 0.01, 0.001]:
        for rc in [1, 0.1, 0.01, 0.001]:
            for ni in [500, 1000]:
                for bs in [32, 64]:
                    bias, weights, error = model_predict(X_train, X_test, y_train, y_test, lr, rc, ni, bs)
                    bias_list.append(bias)
                    weights_list.append(weights)
                    errors.append(error)
                    hyperparameters.append((lr, rc, ni, bs))
    return bias_list, weights_list, errors, hyperparameters

# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for i in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

def cross_validation(dataset, k_folds, l_rate):
    folds = cross_validation_split(dataset, k_folds)
    bias_list = list()
    weights_list = list()
    errors = list()
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])
        X_train, y_train = input_output_split(train_set)
        X_test, y_test = input_output_split(fold)
        bias, weights, error = model_predict(X_train, X_test, y_train, y_test, l_rate)
        bias_list.append(bias)
        weights_list.append(weights)
        errors.append(error)
    return np.array(bias_list), np.array(weights_list), np.array(errors)

def train(data_train, k=5):
    errors_list = list()
    bias_list = list()
    weights_list = list()
    hyperparams_list = list()
    folds = cross_validation_split(data_train, k)
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])
        X_train, y_train = input_output_split(train_set)
        X_test, y_test = input_output_split(fold)
        bias, weights, errors, hyperparameters = choose_hyperparameters(X_train, y_train, X_test, y_test)
        targent_index = np.argmin(errors)
        errors_list.append(errors[targent_index])
        bias_list.append(bias[targent_index])
        weights_list.append(weights[targent_index])
        hyperparams_list.append(hyperparameters[targent_index])
    targent_index = np.argmin(errors_list)
    target_bias_norm = bias_list[targent_index]
    target_weights_norm = weights_list[targent_index]
    target_hyperparams = hyperparams_list[targent_index]
    print(target_hyperparams)
    return target_bias_norm, target_weights_norm

def get_plots_for_regression(df, label='price', save=False):
    cols = list(df.columns)
    cols.remove(label)
    for col in cols:
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.scatter(df[col], df[label], label='Real price', alpha=0.5)
        plt.title(f'Scatter plot of {label} and {col}')
        plt.xlabel(col)
        plt.ylabel(label)
        plt.legend(loc='upper left')
        plt.grid()
        plt.show()
        if save:
            fig.savefig(f'{col}.png')

def plot_results(y, preds, save=False, label='Price'):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    n = len(y)
    ax1.scatter(np.linspace(1, n, n), y, label="Real values", alpha=0.7)
    ax1.scatter(np.linspace(1, n, n), preds, label="Predicted values", alpha=0.7)
    plt.title(f'Scatter plot of {label} for real and predicted values in test set')
    plt.ylabel(label)
    plt.xlabel('n-th example in test set')
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()
    if save:
        fig.savefig(f'{label}_for_test_results.png')

# Load data
data = load_csv('/Users/jelenajaksic/Desktop/psz-projekat/prediction-models/bgd-filtered.csv')
data['rooms'] = data['rooms'].fillna(data['rooms'].median()) 
data['new']=data.apply(lambda x: 1 if x.year==1 else 0, axis=1) 
data['old']=data.apply(lambda x: 1 if x.year==-1 else 0, axis=1) 
data['no_data']=data.apply(lambda x: 1 if x.year==0 else 0, axis=1)
print(data)

#plot
get_plots_for_regression(data, save=True)

# Normalize data
data_min, data_max = dataset_minmax(data)
data = normalize_data(data)

# Split into training and test 
data_train, data_test = train_test_split(data, 0.995)

# Choose hyperparameters and train 
target_bias_norm, target_weights_norm = train(data_train)

# Test
X_test, y_test = input_output_split(data_test)
predicted = np.dot(X_test, target_weights_norm) + target_bias_norm
y_test = rev_normalization(y_test, data_min[4], data_max[4])
predicted = rev_normalization(predicted, data_min[4], data_max[4])
error = mean_square_error(y_test, predicted)

# plot results
plot_results(y_test, predicted, save=True)

print('Data max:', data_max)
print('Data min:', data_min)
print('Bias:', target_bias_norm)
print('Weights:', target_weights_norm)
print('Predicted:', predicted)
print('Actual:', y_test)
print('Error:', error)