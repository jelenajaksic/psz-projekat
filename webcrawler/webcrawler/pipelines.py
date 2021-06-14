# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from webcrawler.webcrawler.db_manager import DbManager
from itemadapter import ItemAdapter

class WebcrawlerPipeline:
    def __init__(self):
        self.db_manager = DbManager()

    def process_item(self, item, spider):
        return item
