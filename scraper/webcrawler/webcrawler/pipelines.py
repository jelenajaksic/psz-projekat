# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from webcrawler.db_manager import DbManager
from itemadapter import ItemAdapter
import pandas as pd
import os
from .db_manager import DbManager


class WebcrawlerPipeline:
    def __init__(self):
        self.db_manager = DbManager.Instance()
        self.con = self.db_manager.create_engine()
        self.a = 'a'

    def process_item(self, item, spider):
        # print(item)
        # df=pd.DataFrame.from_dict(item)
        df = pd.DataFrame([item], columns=["url", "property_type", "location", "block", "distance_from_center", "add_type", "size", "year", "area", "storey", "total_storeys", "registered", "heat_type", "rooms", "toiletes", "parking", "price", "other"])
        # if not os.path.isfile('filename.csv'):
        df.to_sql('realestate', index=False, con=self.con, if_exists='append')
        # else:  # else it exists so append without writing the header
            # df.to_csv('filename.csv', mode='a', header=False, encoding='utf-8-sig', index=False)
