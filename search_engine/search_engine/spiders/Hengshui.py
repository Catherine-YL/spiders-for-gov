from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class HengshuiSpider(ZhengFuBaseSpider):
    name: str = '衡水'
    api: str = 'http://www.hengshui.gov.cn/jrobot/search.do?webid=1&pg=12&p={page}&tpl=&category=&q={keyword}&pos=&od=&date=&date='
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        page = response.css("#jsearch-info-box::attr(data-total)").get()
        return int(page) // 12 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        box = response.css("div#jsearch-result-items > div.jsearch-result-box")
        return box

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.css("div.jsearch-result-title > a::text").getall(),
            'url': item.css("div.jsearch-result-abs > div.jsearch-result-other-info > div.jsearch-result-url > a::text").get(),
            'source': "无",
            'date': item.css("span.jsearch-result-date::text").get(),
        }
        return result

