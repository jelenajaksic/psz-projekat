from django.shortcuts import render
from .lib.db_manager import DbManager
import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def get_all(request):
    db = DbManager.Instance()
    con = db.create_engine()
    df = pd.read_sql("""select * from realestate limit 5""", con=con)
    result = df.to_dict('records')
    return Response(result)


@api_view(['GET'])
def get_most_common(request):
    db = DbManager.Instance()
    con = db.create_engine()
    df_sell = pd.read_sql(
        """select block, count(*) as number from db.realestate where add_type = 's' and location='Beograd' group by block order by number desc limit 10""", con=con)
    result_sell = df_sell.to_dict('records')
    df_rent = pd.read_sql(
        """select block, count(*) as number from db.realestate where add_type = 'r' and location='Beograd' group by block order by number desc limit 10""", con=con)
    result_rent = df_rent.to_dict('records')
    df = pd.read_sql(
        """select block, count(*) as number from db.realestate where location='Beograd' group by block order by number desc limit 10""", con=con)
    result_all = df.to_dict('records')

    result = {
        "sell": result_sell,
        "rent": result_rent,
        "all": result_all
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
