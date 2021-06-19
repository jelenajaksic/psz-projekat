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
    df = pd.read_sql('select * from realestate limit 5', con=con)
    result = df.to_dict('records')
    return Response(result)