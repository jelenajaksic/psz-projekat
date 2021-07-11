import numpy as np

class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000, batch_size=64, regularization_coeff = 0.001):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.batch_size = batch_size
        self.weights, self.bias = None, None
        self.loss = []
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
        # Mini Batch
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
            y_h = np.dot(X, self.weights) + self.bias
            loss = self._mean_squared_error(y, y_h)
            self.loss.append(loss)
            # Batch 
            # # Line equation
            # y_hat = np.dot(X, self.weights) + self.bias
            # loss = self._mean_squared_error(y, y_hat)
            # self.loss.append(loss)
            
            # # Calculate derivatives
            # partial_w = (1 / X.shape[0]) * (2 * np.dot(X.T, (y_hat - y)))
            # partial_d = (1 / X.shape[0]) * (2 * np.sum(y_hat - y))
            
            # # Update the coefficients
            # self.weights -= self.learning_rate * partial_w
            # self.bias -= self.learning_rate * partial_d

            # if i % 100 == 0:
            #     print(i, 'th iteration done')
            #     print([self.bias, self.weights[0], self.weights[1]])
        
        
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
