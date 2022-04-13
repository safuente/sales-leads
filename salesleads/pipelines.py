# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter
from scrapy.exceptions import DropItem
import os


class SalesLeadsPipeline:
    def open_spider(self, spider):
        os.makedirs('data', exist_ok=True)
        self.f = open('data/stores.json', 'wb')
        self.exporter = JsonItemExporter(self.f)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.f.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class DuplicatesPipeline:

    def __init__(self):
        self.websites_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['website'] in self.websites_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.websites_seen.add(adapter['website'])
            return item
