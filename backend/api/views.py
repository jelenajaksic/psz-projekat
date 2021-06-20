from django.shortcuts import render
from .lib.db_manager import DbManager
import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

# Create your views here.


@api_view(['POST'])
def get_all(request):
    db = DbManager.Instance()
    con = db.create_engine()
    body = json.loads(request.body.decode('utf-8'))
    page = body['page']
    itemsPerPage = body['itemsPerPage']
    sortBy = body['sortBy']
    sortDesc = body['sortDesc']
    start = (page-1)*itemsPerPage
    end = page*itemsPerPage

    if len(sortBy) > 0:
        df = pd.read_sql(
            "select * from realestate order by {} {} limit {},{}".format(sortBy[0], 'desc' if sortDesc[0] == True else 'asc', start, itemsPerPage), con=con)
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
        """select block, count(*) as number from db.realestate where add_type = 's' and location='Beograd' group by block order by number desc limit 10""", con=con)
    result_sell_labels = df_sell.block
    result_sell_data = df_sell.number
    df_rent = pd.read_sql(
        """select block, count(*) as number from db.realestate where add_type = 'r' and location='Beograd' group by block order by number desc limit 10""", con=con)
    # result_rent = df_rent.to_dict('records')
    result_rent_labels = df_rent.block
    result_rent_data = df_rent.number
    df = pd.read_sql(
        """select block, count(*) as number from db.realestate where location='Beograd' group by block order by number desc limit 10""", con=con)
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
        'select location, COUNT(*) as number from db.realestate where add_type = \'s\' group by location order by number desc', con=con)
    df.location = df.apply(lambda x: x.location.title(), axis=1)
    result = df.fillna("").to_dict('records')
    return Response(result)

@api_view(['GET'])
def get_registration(request):
    db = DbManager.Instance()
    con = db.create_engine()
    house = pd.read_sql(
        "select registered, count(*) as number from db.realestate where property_type = 'h' group by registered", con=con)
    apartment = pd.read_sql(
        "select registered, count(*) as number from db.realestate where property_type = 'a' group by registered", con=con)
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
