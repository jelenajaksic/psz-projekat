from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from random import randrange

# Load a CSV file
def load_csv(url):
    print('Load data')
    return pd.read_csv(url)

# Find the minimum and maximum for each column
def dataset_minmax(dataset):
	return dataset.min(), dataset.max()

# Normalize data - minmax approach
def normalize_data(data):
    data = (data-data.min())/(data.max()-data.min())
    return data.values.tolist()

# Reverse normalization
def rev_normalization(data_norm, data_min, data_max):
	return data_norm*(data_max-data_min) + data_min

# Row normalizaton
def row_normalization(row, min, max):
	row_norm = list()
	for i in range(len(row)):
		row_norm.append((row[i]-min[i])/(max[i]-min[i]))
	return row_norm

# Calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)

# Calculate the Manhattan distance between two vectors
def manhattan_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += abs(row1[i] - row2[i])
	return distance

# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors, func):
	distances = list()
	for train_row in train:
		dist = func(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors

# Make a prediction with neighbors
def predict_classification(train, test_row, num_neighbors, func):
	neighbors = get_neighbors(train, test_row, num_neighbors, func)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction

def get_plots_for_knn(df, label='class', save=False):
    cols = list(df.columns)
    cols.remove(label)
    for i in range(len(cols)-1):
        for j in range(i+1, len(cols)):
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            for clas in range(1, 6):
                ax1.scatter(df[df[label] == clas][cols[i]],
                            df[df[label] == clas][cols[j]], label=clas, alpha=0.7)
            plt.title(f'Scatter plot of {cols[i]} and {cols[j]}')
            plt.xlabel(cols[i])
            plt.ylabel(cols[j])
            plt.legend(loc='upper right')
            plt.grid()
            plt.show()
            if save:
                fig.savefig(f'{cols[i]}_{cols[j]}.png')

def plot_results(y, preds, save=False, label='Class'):
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

# Make a prediction with KNN
def predict_price_with_knn (num_neighbors = 97):
	print('predict_price_with_knn')

	# Load and ajdust data
	data = load_csv('/Users/jelenajaksic/Desktop/psz-projekat/prediction-models/bgd-filtered.csv')
	data['rooms'] = data['rooms'].fillna(data['rooms'].median()) 
	data['new']=data.apply(lambda x: 1 if x.year==1 else 0, axis=1) 
	data['old']=data.apply(lambda x: 1 if x.year==-1 else 0, axis=1) 
	data['no_data']=data.apply(lambda x: 1 if x.year==0 else 0, axis=1)
	data['class']=data.apply(lambda x: 1 if x.price< 50000  else 2 if x.price < 100000 else 3 if x.price < 150000 else 4 if x.price < 200000 else 5, axis=1)
	data = data.drop("year", axis=1)
	data = data.drop("price", axis=1)

	# plot
	get_plots_for_knn(data, save=True)

	# Normalize data
	data_min, data_max = dataset_minmax(data)
	data = normalize_data(data)
	# Split into training and test 
	data_train, data_test = train_test_split(data, 0.995)

	y_test = list()
	for j in data_test:
		y_test.append(rev_normalization(j[-1], data_min[-1], data_max[-1]))
		del j[-1]

	# predict the label
	labels_euc = list()
	labels_man = list()
	for i in range(len(data_test)):
		label_euc = predict_classification(data_train, data_test[i], num_neighbors, euclidean_distance)
		label_man = predict_classification(data_train, data_test[i], num_neighbors, manhattan_distance)
		label_euc = int(label_euc * (data_max[-1] - data_min[-1]) + data_min[-1])
		label_man = int(label_man * (data_max[-1] - data_min[-1]) + data_min[-1])
		labels_euc.append(label_euc)
		labels_man.append(label_man)

	# plot results
	plot_results(y_test, labels_euc, label='Class Euc', save=True)
	plot_results(y_test, labels_man, label='Class Man', save=True)

predict_price_with_knn()