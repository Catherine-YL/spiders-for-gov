from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class XuchangSpider(ZhengFuBaseSpider):
    name: str = '许昌'
    api: str = 'http://www.xuchang.gov.cn/inteligentsearch/rest/esinteligentsearch/getFullTextDataNew'
    method: str = 'POST'
    json_mode = True
    headers: dict[str, str] = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
    }
    data: dict[str, Any] =  {
        "token":"",
        "pn":"20",
        "rn":"10",
        "sdt":"",
        "edt":"",
        "wd":"{keyword}",
        "inc_wd":"",
        "exc_wd":"",
        "fields":"title;content",
        "cnum":"",
        "sort":"",
        "ssort":"title",
        "cl":500,
        "terminal":"",
        "condition":None,
        "time":None,
        "highlights":"title;content",
        "statistics":None,
        "unionCondition":None,
        "accuracy":"",
        "noParticiple":"0",
        "searchRange":None,
    }
    debug: bool = False
    cate_dict = {
        "001": "新闻中心",
        "002": "信息公开",
        "003": "许昌要闻",
        "004": "部门动态",
        "005": "区县动态",
        "006": "其他",
        "007": "通知通告",
    }


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        data = response.json()
        page = data["result"]["totalcount"]
        return int(page) // 10 + 1

    def edit_data(self, data: dict, keyword: str, page: int, **kwargs) -> dict[str, Any]:
        data["pn"] = 10 * (page - 1)
        return data

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        data = response.json()
        return data["result"]["records"]

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        url = item["linkurl"]
        if "http" in url:
            result = {
                'title': item["title"],
                'url': item["linkurl"],
                'source': self.cate_dict.get(item["syscategory"], "无"),
                'date': item["showdate"],
            }
        else:
            result = {
                'title': item["title"],
                'url': 'http://www.xuchang.gov.cn' + item["linkurl"],
                'source': self.cate_dict.get(item["syscategory"], "无"),
                'date': item["showdate"],
            }
        return result

