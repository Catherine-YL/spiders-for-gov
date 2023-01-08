from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A山东省生态环境厅Spider(ZhengFuBaseSpider):
    name: str = '山东省生态环境厅'
    api: str = 'http://sthj.shandong.gov.cn/was5/web/search?page={page}&channelid=237677&searchword={keyword}&keyword={keyword}&perpage=10&outlinepage=10&andsen=&total=&orsen=&exclude=&searchscope=&timescope=&orderby=-DOCRELTIME'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.css("ul.clearfix li.relative-cs span::text").get()
        return int(total) // 10 + 1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("div.search-inform div.iteminform")

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
            'title': item.css("div.iteminform-top a::text").get(),
            'url': item.css("div.iteminform-top a::attr(href)").get(),
            'type': item.css("div.iteminform-top span::text").get(),
            'date': item.css("div.iteminform-time::text").get().split("：")[1],
        }
        return result

