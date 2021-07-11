import numpy as np
from random import randrange
from .model import LinearRegression

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
    for lr in [0.5, 0.1, 0.01, 0.001]:
        for rc in [0.5, 0.1, 0.01, 0.001]:
            for ni in [500, 1000, 5000]:
                for bs in [16, 32, 64]:
                    bias, weights, error = model_predict(X_train, X_test, y_train, y_test, lr, rc, ni, bs)
                    bias_list.append(bias)
                    weights_list.append(weights)
                    errors.append(error)
                    hyperparameters.append((lr, rc, ni, bs))
    return bias_list, weights_list, errors, hyperparameters

def train(X_train, y_train, X_test, y_test):
    bias_list, weights_list, errors, hyperparameters = choose_hyperparameters(X_train, y_train, X_test, y_test)
    targent_index = np.argmin(errors)
    target_bias_norm = bias_list[targent_index]
    target_weights_norm = weights_list[targent_index]
    target_hyperparams = hyperparameters[targent_index]
    print(target_hyperparams)
    return target_bias_norm, target_weights_norm