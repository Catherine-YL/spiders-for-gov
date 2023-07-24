from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector
from typing import Any, Generator, Iterable, List, Optional, Union
from functools import reduce

class s三明Spider(ZhengFuBaseSpider):
    name = "三明"
    method = "POST"
    allowed_domains = ['sm.gov.cn']
    start_urls = ['http://www.sm.gov.cn']
    api = "http://www.sm.gov.cn/ssp/search/api/search?time=1689824448647"
    data = {
        "siteType": "1",
        "mainSiteId": "ff808081744e1c2301744e1e83600002",
        "siteId": "ff808081744e1c2301744e1e83600002",
        "type": "0",
        "page": "{page}",
        "rows": "10",
        "historyId":"",
        "sourceType": "SSP_ZHSS",
        "isChange": "0",
        "fullKey": "N",
        "wbServiceType": "13",
        "fileType":"",
        "fileNo":"",
        "pubOrg":"",
        "themeType":"",
        "searchTime":"",
        "startDate":"",
        "endDate":"",
        "sortFiled": "RELEVANCE",
        "searchFiled":"",
        "dirUseLevel":"",
        "issueYear":"",
        "issueMonth":"",
        "allKey":"",
        "fullWord":"",
        "oneKey":"",
        "notKey":"",
        "totalIssue":"",
        "chnlName":"",
        "zfgbTitle":"",
        "zfgbContent":"",
        "zfgbPubOrg":"",
        "keyWord": "{keyword}",
    }
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    debug = False
    def edit_data(self, data: dict, keyword: str, page: int) -> dict:
        """
        返回POST数据.
        """
        data["keyWord"] = keyword
        data["page"] = str(page)
        return data
    def edit_page(self, response: Response) -> int:
        pages = response.json()['page']['pagecount']
        return int(pages)

    def edit_items_box(self, response: Response) -> Union[Any, Iterable[Any]]:
        return response.json()['datas']

    def edit_items(self, items_box: Any) -> Iterable[Any]:
        """
        从items容器中解析出items的迭代容器
        input: items_box
        return: items
        """
        return [item for item in items_box]

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        data = {
            'url': item['docpuburl'],
            'date':item['docreltime'],
            'title':item['_doctitle'],
            'type':item.get('sourceType'),
            'source':item['docsourcename']
        }
        return data