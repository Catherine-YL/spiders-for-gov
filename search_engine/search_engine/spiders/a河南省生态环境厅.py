from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector
import urllib
from urllib import parse
class A河南省生态环境厅Spider(ZhengFuBaseSpider):
    name: str = '河南省生态环境厅'
    api: str = 'https://search1.henan.gov.cn/jrobot/search.do?_cus_lq_field_107=&_cus_eq_field_105=&_cus_eq_field_110=&_cus_pq_content=&_cus_eq_field_118=&_cus_eq_field_119=&_cus_eq_field_108=&_cus_eq_field_111=&_cus_eq_field_113=&_cus_eq_field_112=&webid=10020&pg=12&p={page}&tpl=&category=&_cus_query=&_cus_pq_content=&q={keyword}&pos=title&od=&date=&date='
    method: str = 'GET'
    data: dict[str, Any] = {}
    start_page: int = 0
    debug: bool = False

    def edit_page(self, response: Selector) -> int:
        total = response.css("#jsearch-info-box::attr(data-total) ").get()
        print(total)
        return int(total)

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("div.jsearch-result-box")

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        try:
            url= item.css("div.jsearch-result-title > a::attr(href)").re('url=(.*)&q=')[0]
            url = str(url)
            new_txt = urllib.parse.unquote(url)
        except:
            new_txt= item.css("div.jsearch-result-title > a::attr(href)").get()
        result = {
            'title': item.css("div.jsearch-result-title a::text").getall(),
            'url': new_txt,
            'date': item.css("span.jsearch-result-date::text").get(),
        }
        return result