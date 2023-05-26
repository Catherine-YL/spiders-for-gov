from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector
import json
import re


class A湘潭Spider(ZhengFuBaseSpider):
    name: str = '湘潭'
    api: str = 'http://searching.hunan.gov.cn:8977/hunan/974000000/news?q={keyword}&searchfields=&sm=0&columnCN=&iszq=&aggr_iszq=&p={page}&timetype=timeqb'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
    }

    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        # response.json()["searchResultAll"]["searchTotal"][0]
        page = response.css("body > div.content > div > div.main-content > div.choose > div > div.time-limit.result > p::text").get()
        a = []
        a = re.findall("\d+\.?\d*", page)
        page =int(a[0])
        page = page//10+1

        return page

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        return response.css("#hits")
    def edit_items(self, items_box: Any) -> Iterable[Any]:
        """
        从items容器中解析出items的迭代容器
        input: items_box
        return: items
        """
        return items_box.css("#hits > li")

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        result = {
            'title': item.css("div.com-title > div > a::attr(title)").getall(),
            'url': item.css("div.com-title > div > a::attr(href)").get(),
            'source': item.css("div.right > div > span.source-name::text").get(),
            'date': item.css("div.right > div > span.source-time::text").get(),
        }
        return result