from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector
import json
import time

class A新疆维吾尔自治区生态环境厅Spider(ZhengFuBaseSpider):
    name: str = '新疆维吾尔自治区生态环境厅'
    api: str = 'http://www.xinjiang.gov.cn/guestweb/sHtml'
    method: str = 'POST'
    data: dict[str, Any] = {}
    debug: bool = False
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
    }
    data = {
        "searchWord": "{keyword}",
        "siteCode": "6500000003",
        "column": "%E5%85%A8%E9%83%A8",
        "wordPlace": "",
        "orderBy": "0",
        "startTime":"",
        "endTime":"",
        "pageSize": "10",
        "pageNum": "{page}",
        "timeStamp": "0",
        "sonSiteCode":"",
        "checkHandle": "1",
        "strFileType": "全部格式",
        "areaSearchFlag":"",
        "secondSearchWords":"",
        "countKey": "0",
        "uc": "1",
        "userName": "81YZbrfJ2Lwgj25nLY5IeA==",
        "passWord": "6/hZqnPJzHtfxu+V+PtxuA=="
    }

    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        # response.json()["searchResultAll"]["searchTotal"][0]
        page = int(response.json()["searchResultAll"]["total"])

        return page//10+1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        time.sleep(1)
        return response.json()["searchResultAll"]["searchTotal"]

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
            'type': item["source"],
            'date': item["pubDate"]
        }
        return result
