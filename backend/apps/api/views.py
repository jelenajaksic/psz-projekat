from django.shortcuts import render
from .lib.db_manager import DbManager
import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from math import sqrt


@api_view(['POST'])
def get_all(request):
    db = DbManager.Instance()
    con = db.create_engine()
    body = json.loads(request.body.decode('utf-8'))
    page = body['page']
    itemsPerPage = body['itemsPerPage']
    sortBy = body['sortBy']
    sortDesc = body['sortDesc']
    start = (page - 1) * itemsPerPage
    end = page * itemsPerPage

    if len(sortBy) > 0:
        df = pd.read_sql(
            "select * from realestate order by {} {} limit {},{}".format(sortBy[0],
                                                                         'desc' if sortDesc[0] == True else 'asc',
                                                                         start, itemsPerPage), con=con)
    else:
        df = pd.read_sql(
            "select * from realestate limit {},{}".format(start, itemsPerPage), con=con)
    result = df.fillna("").to_dict('records')
    return Response(result)


@api_view(['GET'])
def get_most_common(request):
    db = DbManager.Instance()
    con = db.create_engine()
    df_sell = pd.read_sql(
        """select block, count(*) as number from db.realestate where add_type = 's' and location='Beograd' group by 
        block order by number desc limit 10""",
        con=con)
    result_sell_labels = df_sell.block
    result_sell_data = df_sell.number
    df_rent = pd.read_sql(
        """select block, count(*) as number from db.realestate where add_type = 'r' and location='Beograd' group by 
        block order by number desc limit 10""",
        con=con)
    # result_rent = df_rent.to_dict('records')
    result_rent_labels = df_rent.block
    result_rent_data = df_rent.number
    df = pd.read_sql(
        """select block, count(*) as number from db.realestate where location='Beograd' group by block order by 
        number desc limit 10""",
        con=con)
    # result_all = df.to_dict('records')
    result_all_labels = df.block
    result_all_data = df.number

    result = {
        "sell": {"labels": result_sell_labels, "data": result_sell_data},
        "rent": {"labels": result_rent_labels, "data": result_rent_data},
        "all": {"labels": result_all_labels, "data": result_all_data}
    }

    return Response(result)


@api_view(['GET'])
def get_props_by_size(request):
    db = DbManager.Instance()
    con = db.create_engine()
    df = pd.read_sql("""
    select x, count(*) as y from
	(SELECT size,
	CASE
		WHEN size <= 35 THEN 'Less than 35'
		WHEN size > 35 and size <= 50 THEN '36 - 50'
		WHEN size > 50 and size <= 65 THEN '51 - 65'
		WHEN size > 65 and size <= 80 THEN '66 - 80'
		WHEN size > 80 and size <= 95 THEN '81 - 95'
		WHEN size > 95 and size <= 110 THEN '96 - 110'
		WHEN size > 110 THEN 'More than 110'
    ELSE 'No size data'
	END AS x
	FROM db.realestate) a
    group by x
    """, con=con)
    result = df.to_dict('records')
    return Response(result)


@api_view(['GET'])
def get_props_by_year(request):
    db = DbManager.Instance()
    con = db.create_engine()
    df = pd.read_sql("""
    select x, count(*) as y from
	(SELECT year,
	CASE
		WHEN year < 1950 THEN 'Before 1951'
		WHEN year > 1950 and year <= 1960 THEN '1951 - 1960'
		WHEN year > 1960 and year <= 1970 THEN '1961 - 1970'
		WHEN year > 1970 and year <= 1980 THEN '1971 - 1980'
		WHEN year > 1980 and year <= 1990 THEN '1981 - 1990'
		WHEN year > 1990 and year <= 2000 THEN '1991 - 2000'
		WHEN year > 2000 and year <= 2010 THEN '2001 - 2010'
		WHEN year > 2010 and year <= 2020 THEN '2011 - 2020'
		WHEN year > 2020 THEN 'Aftrer 2021 (under construction)'
	END AS x
	FROM db.realestate) a
    where x is not null
    group by x   
    """, con=con)
    result = df.to_dict('records')
    return Response(result)


@api_view(['GET'])
def get_number_of_properties(request):
    db = DbManager.Instance()
    con = db.create_engine()
    df = pd.read_sql(
        'select count(*) as num from db.realestate where add_type = \'s\'', con=con)
    sell = df.num.iloc[0]
    df = pd.read_sql(
        'select count(*) as num from db.realestate where add_type = \'r\'', con=con)
    rent = df.num.iloc[0]
    df = pd.read_sql('select count(*) as num from db.realestate', con=con)
    all = df.num.iloc[0]
    result = {
        "sell": sell,
        "rent": rent,
        "all": all
    }
    return Response(result)


@api_view(['GET'])
def get_number_of_properties_by_city(request):
    db = DbManager.Instance()
    con = db.create_engine()
    df = pd.read_sql(
        'select location, COUNT(*) as number from db.realestate where add_type = \'s\' group by location order by number desc',
        con=con)
    df.location = df.apply(lambda x: x.location.title(), axis=1)
    result = df.fillna("").to_dict('records')
    return Response(result)


@api_view(['GET'])
def get_registration(request):
    db = DbManager.Instance()
    con = db.create_engine()
    house = pd.read_sql(
        "select registered, count(*) as number from db.realestate where property_type = 'h' group by registered",
        con=con)
    apartment = pd.read_sql(
        "select registered, count(*) as number from db.realestate where property_type = 'a' group by registered",
        con=con)
    h = house.fillna("").to_dict('records')
    a = apartment.fillna("").to_dict('records')
    print(h[2])
    result = {
        'houses': {
            'registered': h[2]['number'],
            'unregistered': h[1]['number'],
            'nodata': h[0]['number']
        },
        'apartments': {
            'registered': a[2]['number'],
            'unregistered': a[1]['number'],
            'nodata': a[0]['number']
        }
    }
    return Response(result)


@api_view(['GET'])
def get_sell_rent_ratio(request):
    db = DbManager.Instance()
    con = db.create_engine()
    df = pd.read_sql("""
    select location, sell, rent, sell/rent, sell+rent as total from
	(select a.location as location, a.sell as sell, b.rent as rent from 
		(select location, count(*) as sell from db.realestate where add_type='s' group by location) as a
		left join
		(select location, count(*) as rent from db.realestate where add_type='r' group by location) as b 
		on a.location=b.location
	) a
    where location in 
        (select location from 
            (select location, count(*) as number from db.realestate group by location order by number desc limit 5) a
        )  
    """, con=con)
    result = df.to_dict('records')
    return Response(result)


@api_view(['GET'])
def get_props_by_price_category(request):
    db = DbManager.Instance()
    con = db.create_engine()
    df = pd.read_sql("""
    select x, count(*) as y from
        (SELECT price,
        CASE
            WHEN price < 49999 THEN 'Less then 49,999'
            WHEN price >= 50000 and price <= 99999 THEN '50,000 - 99,999'
            WHEN price >=100000 and price <= 149999 THEN '100,000 - 149,999'
            WHEN price >= 150000 and price <= 199999 THEN '150,000 - 199,999'
            WHEN price >=200000 THEN 'Greater then 200,000'
        ELSE 'No price data'
        END AS x
        FROM db.realestate where add_type='s') a
    group by x 
    """, con=con)
    result = df.fillna("").to_dict('records')
    return Response(result)


@api_view(['GET'])
def get_number_of_properties_with_parking(request):
    db = DbManager.Instance()
    con = db.create_engine()
    df = pd.read_sql("""
    select count(*) as parking from db.realestate where parking = 1 and add_type ='s' and location='Beograd'
    union
    select count(*) from db.realestate where add_type ='s' and location='Beograd'
    """, con=con)
    result = df.to_dict('list')
    return Response(result)


@api_view(['GET'])
def get_top_30(request):
    db = DbManager.Instance()
    con = db.create_engine()
    df_a = pd.read_sql("""
    select location, price, url from db.realestate where property_type='a' and add_type='s' order by price desc limit 30
    """, con=con)
    df_h = pd.read_sql("""
    select location, price, url from db.realestate where property_type='h' and add_type='s' order by price desc limit 30
    """, con=con)
    result_a = df_a.fillna("").to_dict('records')
    result_h = df_h.fillna("").to_dict('records')
    result = {
        "houses": result_h,
        "apartments": result_a
    }
    return Response(result)


@api_view(['GET'])
def get_top_100(request):
    db = DbManager.Instance()
    con = db.create_engine()
    df_a = pd.read_sql("""
    select property_type, location, size, price, url from db.realestate where property_type='a' order by size desc limit 100
    """, con=con)
    df_h = pd.read_sql("""
    select property_type, location, size, price, url from db.realestate where property_type='h' order by size desc limit 100
    """, con=con)
    result_a = df_a.fillna("").to_dict('records')
    result_h = df_h.fillna("").to_dict('records')
    result = {
        "houses": result_h,
        "apartments": result_a
    }
    return Response(result)


@api_view(['GET'])
def get_2020(request):
    db = DbManager.Instance()
    con = db.create_engine()
    df_r = pd.read_sql("""
    select property_type, location, size, price, url from db.realestate where add_type='r' and year=2020 order by price desc
    """, con=con)
    df_s = pd.read_sql("""
    select property_type, location, size, price, url from db.realestate where add_type='s' and year=2020 order by price desc
    """, con=con)
    result_s = df_s.fillna("").to_dict('records')
    result_r = df_r.fillna("").to_dict('records')
    result = {
        "sell": result_s,
        "rent": result_r
    }
    return Response(result)


@api_view(['GET'])
def get_top_30_rooms_area(request):
    db = DbManager.Instance()
    con = db.create_engine()
    df_r = pd.read_sql("""
    select location, property_type, add_type, price, rooms, url from db.realestate order by rooms desc limit 30
    """, con=con)
    df_a = pd.read_sql("""
    select location, add_type, area, price, url from db.realestate where property_type='h' order by area desc limit 30
    """, con=con)
    result_r = df_r.fillna("").to_dict('records')
    result_a = df_a.fillna("").to_dict('records')
    result = {
        "rooms": result_r,
        "area": result_a
    }
    return Response(result)


@api_view(['POST'])
def predict_with_linear_regression(request):
    bias = 0.08944277879143522
    weights = [0.53251661, -0.34636063, 0.27110472, 0.01596352, -0.0174907, 0.00358648]
    min_price = 10000
    max_price = 145000
    body = json.loads(request.body.decode('utf-8'))
    size = body['size']
    dist = body['dist']
    rooms = body['rooms']
    old = body['old']
    new = body['new']
    nodata = body['nodata']
    price = bias + weights[0] * size + weights[1] * dist + weights[2] * rooms + weights[3] * old + weights[4] * new + \
            weights[0] * nodata
    price = price * (max_price - min_price) + min_price
    price = round(price, 0)
    return Response(price)


@api_view(['POST'])
def predict_with_knn(request):
    default_k = 101
    body = json.loads(request.body.decode('utf-8'))
    k_nbrs = body['k_nbrs'] if body['k_nbrs'] else default_k
    prop = [body['size'], body['dist'], body['rooms'], body['new'], body['old'], body['nodata']]
    price_euc, price_man = predict_price_with_knn(prop, k_nbrs)
    res = {
        "res_euc": price_euc,
        "res_man": price_man
    }
    return Response(res)


### KNN model

# Find the minimum and maximum for each column
def dataset_minmax(dataset):
    return dataset.min(), dataset.max()


# Normalize data - minmax approach
def normalize_data(data):
    data = (data - data.min()) / (data.max() - data.min())
    return data.values.tolist()


# Row normalization
def row_normalization(row, min, max):
    row_norm = list()
    for i in range(len(row)):
        row_norm.append((row[i] - min[i]) / (max[i] - min[i]))
    return row_norm


# Calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1) - 1):
        distance += (row1[i] - row2[i]) ** 2
    return sqrt(distance)


# Calculate the Manhattan distance between two vectors
def manhattan_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1) - 1):
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
def predict_price_with_knn(prop, num_neighbors=97):
    # Load and ajdust data
    db = DbManager.Instance()
    con = db.create_engine()
    data = pd.read_sql("""
    select * from db.knn
    """, con=con)
    data['rooms'] = data['rooms'].fillna(data['rooms'].median())
    data['new'] = data.apply(lambda x: 1 if x.year == 1 else 0, axis=1)
    data['old'] = data.apply(lambda x: 1 if x.year == -1 else 0, axis=1)
    data['no_data'] = data.apply(lambda x: 1 if x.year == 0 else 0, axis=1)
    data['class'] = data.apply(lambda
                                   x: 1 if x.price < 50000 else 2 if x.price < 100000 else 3 if x.price < 150000 else 4 if x.price < 200000 else 5,
                               axis=1)
    data = data.drop("year", axis=1)
    data = data.drop("price", axis=1)

    # Normalize data
    data_min, data_max = dataset_minmax(data)
    data = normalize_data(data)

    prop = row_normalization(prop, data_min, data_max)

    # # predict the label
    label_euc = predict_classification(data, prop, num_neighbors, euclidean_distance)
    label_man = predict_classification(data, prop, num_neighbors, manhattan_distance)

    label_euc = int(label_euc * (data_max[-1] - data_min[-1]) + data_min[-1])
    label_man = int(label_man * (data_max[-1] - data_min[-1]) + data_min[-1])

    return label_euc, label_man
