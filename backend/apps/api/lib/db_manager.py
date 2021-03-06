from sqlalchemy import create_engine
import os 
import json
import pandas as pd

class Singleton:
    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)


@Singleton
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
