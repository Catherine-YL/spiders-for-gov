#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.commands import ScrapyCommand
from scrapy.exceptions import UsageError
from scrapy.utils.project import get_project_settings
from pymongo import MongoClient
from csv import DictWriter
import logging

logging.getLogger('scrapy.utils.log').disabled = True

class Command(ScrapyCommand):

    def short_desc(self):
        return "获取爬虫当前待爬取的url"

    def save(self, city: str):

        client = MongoClient(get_project_settings().get('MONGODB_URI'))

        filter={
            'content': {'$exists': False}
        }

        project={
            'url': 1, 
            '_id': 0
        }

        sort=list({
            'url': 1
        }.items())

        result = client['scrapy_doc'][city].find(
          filter=filter,
          projection=project,
          sort=sort
        )

        with open(file="data/dumps/{0}.csv".format(city), mode="w", encoding="utf-8") as f:
            csv_writer = DictWriter(f, fieldnames=['url'])
            csv_writer.writeheader()
            for item in result:
                if 'http' in item['url']:
                    csv_writer.writerow(item)

        total_doc_num = client['scrapy_doc'][city].count_documents(filter={})
        content_doc_num = client['scrapy_doc'][city].count_documents(filter={'content': {'$exists': True}})

        print("[coverage: {0:>6.2%} ]: dumps into data/dumps/{1}.csv".format(content_doc_num/total_doc_num, city))

    def run(self, args, opts):
        for city in args:
            self.save(city)
