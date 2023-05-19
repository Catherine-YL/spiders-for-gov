from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector
import json
import time

class A黑龙江省生态环境厅Spider(ZhengFuBaseSpider):
    name: str = '黑龙江省生态环境厅'
    api: str = 'http://221.212.115.3:8888/search/advancedSearch.jspx'
    method: str = 'POST'
    data: dict[str, Any] = {}
    debug: bool = False
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42",
        "Host": "221.212.115.3:8888",
        "Origin": "http://221.212.115.3:8888",
        "Accept": "application/json, text/javascript, */*; q=0.01"
    }
    data = {
        "content": "{keyword}",
        "pageNo": "{page}",
        "pageSize": "10"
    }
    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        data1 = response.json()

        # total = response.css("div.search-jg p span::text").get()
        page = int(data1["total"])
        return page

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        time.sleep(1)
        return response.json()["data"]

    def edit_items(self, items_box: Any) -> Iterable[Any]:
        return [item for item in items_box]

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        time.sleep(1)
        result = {
            'title': item["title"],
            'url':  item["url"],
            'type': item["channel"],
            'date': item["releaseDate"]
        }
        return result
