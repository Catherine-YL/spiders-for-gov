from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A驻安徽省生态环境厅Spider(ZhengFuBaseSpider):
    name: str = '安徽省生态环境厅'
    api: str = 'https://sthjt.ah.gov.cn/site/search/6788031?isAllSite=false&platformCode=anhui_szbm_5&siteId=6788031&columnId=&columnIds=&typeCode=articleNews,pictureNews,videoNews,policyDoc,explainDoc,messageBoard,interviewInfo,collectInfo,survey,public_content&beginDate=&endDate=&fromCode=&keywords={keyword}&excColumns=&datecode=&sort=intelligent&type=&tableColumnId=&subkeywords=&ssqdDeptCode=&ssqdZoneCode=&orderType=0&indexNum=&fileNum=&pid=&language=cn&flag=false&searchType=&searchTplId=&fuzzySearch=true&internalCall=&pageIndex={page}&pageSize=10'
    method: str = 'GET'
    data: dict[str, Any] = {}
    debug: bool = False

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
    }

    def edit_page(self, response: Selector) -> int:
        num1 = int(response.css("body > div.ind_body.wza-container > div.container > div.containerbox > div > div.rightbar.wza-region_info > div:nth-child(2) > ul > li:nth-child(1) > a > span::text").get())
        num2 =int(response.css("body > div.ind_body.wza-container > div.container > div.containerbox > div > div.rightbar.wza-region_info > div:nth-child(2) > ul > li:nth-child(3) > a > span::text").get())
        num3 = int(response.css("body > div.ind_body.wza-container > div.container > div.containerbox > div > div.rightbar.wza-region_info > div:nth-child(2) > ul > li:nth-child(5) > a > span::text").get())
        return int(num3+num2+num1)//10+1

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("body > div.ind_body.wza-container > div.container > div.containerbox > div > div.leftbar > div.searchlistw")

    def edit_items(self, items_box: Any) -> Iterable[Any]:
        """
        从items容器中解析出items的迭代容器
        input: items_box
        return: items
        """
        return items_box.css("ul ")

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.css("li.search-title a::text").getall(),
            'source':item.css("li.search-resources span.author::text").get(),
            'url': item.css("li.search-url a::attr(href)").get(),
            'date': item.css("li.search-resources span.date::text").get(),
        }
        return result
