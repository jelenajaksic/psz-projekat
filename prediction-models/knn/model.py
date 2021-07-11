from math import sqrt
import pandas as pd

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

# Make a prediction with KNN on Iris Dataset
def predict_price_with_knn (property, num_neighbors = 97):
	# Load and ajdust data
	data = load_csv('/Users/jelenajaksic/Desktop/psz-projekat/prediction-models/bgd_ne.csv')
	data['rooms'] = data['rooms'].fillna(data['rooms'].median()) 
	data['new']=data.apply(lambda x: 1 if x.year==1 else 0, axis=1) 
	data['old']=data.apply(lambda x: 1 if x.year==-1 else 0, axis=1) 
	data['no_data']=data.apply(lambda x: 1 if x.year==0 else 0, axis=1)
	data['class']=data.apply(lambda x: 1 if x.price< 50000  else 2 if x.price < 100000 else 3 if x.price < 150000 else 4 if x.price < 200000 else 5, axis=1)
	data = data.drop("year", axis=1)
	data = data.drop("price", axis=1)

	# Normalize data
	data_min, data_max = dataset_minmax(data)
	data = normalize_data(data)
	
	property = row_normalization(property, data_min, data_max)

	# # predict the label
	label_euc = predict_classification(data, property, num_neighbors, euclidean_distance)
	label_man = predict_classification(data, property, num_neighbors, manhattan_distance)

	label_euc = int(label_euc * (data_max[-1] - data_min[-1]) + data_min[-1])
	label_man = int(label_man * (data_max[-1] - data_min[-1]) + data_min[-1])

	print(f'Predicted with euc: {label_euc}')
	print(f'Predicted with man: {label_man}')
	return label_euc

predict_price_with_knn([100, 1, 4, 0, 1, 0])