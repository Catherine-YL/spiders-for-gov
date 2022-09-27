from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A漯河Spider(ZhengFuBaseSpider):
    name: str = '漯河'
    api: str = 'http://www.luohe.gov.cn/search/SolrSearch/searchData'
    method: str = 'POST'
    data: dict[str, Any] = {}
    debug: bool = False
    headers: dict[str, str] = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50",
        "Referer": "http://www.luohe.gov.cn/search/SolrSearch/s"
    }
    data = {
        "sword": "{keyword}",
        "newspage": "1",
        "filepage": "1",
        "govpage": "1",
        "picpage": "1",
        "videopage": "1",
        "otherpage": "{page}",
        "orderby": "2",
        "searchMode": "",
        "showMode": "0",
        "searchColumn": "",
        "StringEncoding": "utf-8",
    }

    def edit_page(self, response: Response) -> int:
        """
        返回解析页数.
        """
        # print(response.css('div.dressingBy > font'))
        return response.css('div.browser-body > div.head > div.dressingBy > font').get()

    def edit_data(self, data: dict, keyword: str, page: int) -> dict:
        """
        返回POST数据.
        """
        data["sword"] = keyword
        data["otherpage"] = str(page)
        return data

    def edit_items_box(self, response: Response) -> Selector:
        """
        返回目录索引.
        返回 Selector
        """
        frame = response.css("div.onlyUseToVoice:not(.hide)")
        return frame.css("div.search-result-cntbox > div.srt-container")

    def edit_item(self, item: Selector) -> dict:
        """
        从迭代器中提取item.
        """
        result = {
            'title': item.css("div.result_info_box > a::text").getall(),
            'url': item.css("div.result_info_box  > a::attr(href)").get(),
            'source': item.css("div.rst-ft > span:nth-child(1)::text").get(),
            'date': item.css("div.info_btm > span:nth-child(2)::text").get(),
        }
        return result
