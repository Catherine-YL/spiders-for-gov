from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector
import requests


class TokenMiddleware:
    def __init__(self) -> None:
        self.api = "http://www.luohe.gov.cn/search/SolrSearch/s"
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

    def fetch_token(self, keyword: str):
        resp = requests.post(url=self.api, headers=self.headers, data={"q": keyword})
        s = Selector(text=resp.text)
        return s.css("input[name=token4]::attr(value)").get()


class A漯河Spider(ZhengFuBaseSpider):
    name: str = '漯河'
    api: str = 'http://www.luohe.gov.cn/search/SolrSearch/s'
    method: str = 'POST'
    data: dict[str, Any] = {
        "q": "{keyword}",
        "type": "",
        "timeType": "",
        "sort": "",
        "order": "",
        "forCatalogType": "0",
        "token4": "",
        "siteId": "efc127c860d248459e9b75bc458977d7",
        "offset": "20",
        "limit": "10",
        "infoType": "",
    }
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        raise NotImplementedError()

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        raise NotImplementedError()

    def edit_items(self, items_box: Any) -> Iterable[Any]:
        """
        从items容器中解析出items的迭代容器
        input: items_box
        return: items
        """
        return items_box

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': ,
            'url': ,
            'source': ,
            'date': ,
        }
        return result

