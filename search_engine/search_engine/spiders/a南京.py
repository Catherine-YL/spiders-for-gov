from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector
import json
import re

class A南京Spider(ZhengFuBaseSpider):
    name: str = '南京'
    api: str = 'https://www.nanjing.gov.cn/igs/front/search.jhtml?code=c1c8a0a187b3404a9e7e1b048f90610c&pageNumber={page}&pageSize=10&searchWord={keyword}&searchWord2={keyword}&siteId=10'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
    }
    def edit_page(self, response: Selector) -> int:
        page = int( response.json()["page"]["totalPages"])
        return page

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        return response.json()["page"]["content"]

    def edit_items(self, items_box: Any) -> Iterable[Any]:
        return [item for item in items_box]

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        title = str(item['title'])
        title = title.replace('</em>','')
        title=title.replace('<em>','')

        result = {
            'title': title,
            'url':  item["url"],
            'type': item["trs_type"],
            'date': item["docreltime"],
            'source':item["trs_site"]
        }
        return result