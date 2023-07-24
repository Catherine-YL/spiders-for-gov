#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.utils.project import get_project_settings
from pymongo import MongoClient

class RequestGenerator:
    def __init__(self, name: str) -> None:
        self.name = name
        self.client = MongoClient(get_project_settings().get('MONGODB_URI'))

    def set_name(self, name: str):
        self.name = name

    def fetch_url(self):
        filter={
            'content': {
                '$exists': False
            }
        }
        project={
            'url': 1, 
            '_id': 0
        }
        sort=list({
            'url': 1
        }.items())

        result = self.client['scrapy_doc'][self.name].find(
          filter=filter,
          projection=project,
          sort=sort
        )
        for item in result:
            if 'http' in item['url']:
                yield item
