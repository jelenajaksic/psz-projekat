from sqlalchemy import create_engine
import os 
import json
import pandas as pd


class DbManager():
    def __init__(self) -> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        config=json.load(open(os.path.join(dir_path, 'db_config.json')))
        self.host=config["host"]
        self.port=config["port"]
        self.user=config["user"]
        self.password=config["password"]
        self.db=config["db"]
    
    def create_engine(self):
        return create_engine("mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(self.user, self.password, self.host, self.port, self.db))

# a=DbManager()
# engine=a.create_engine()
# print(engine)

# d = {'col1': [1, 2], 'col2': [3, 4]}
# df = pd.DataFrame(data=d)

# df.to_sql('test', con=engine)