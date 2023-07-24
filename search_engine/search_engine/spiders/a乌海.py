from scrapy.responsetypes import Response
from search_engine.basepro import ZhengFuBaseSpider

class WuhaiSpider(ZhengFuBaseSpider):
    """TODO crawl"""
    name = '乌海'
    api = "http://www.wuhai.gov.cn/search/pcRender?pageId=63493493b61047b8be9bc396fa236e60"
    method = "POST"
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    debug =False
    allowed_domains = ['wuhai.gov.cn']
    start_urls = ['http://www.wuhai.gov.cn']
    data = {
        "originalSearchUrl": "/search/pcRender?pageId=63493493b61047b8be9bc396fa236e60",
        "originalSearch": "",
        "app": "2d2145bfde734f20b3a746f5040a2752,b46547d5770e4c1794e9a337836ba34d,ab217b6d91d64085bd05924b218abbc8,4536d378b2a843d79ad0cbb2d5433ce1,fcff548c7a114dd3b3970d3866191820",
        "appName": "",
        "sr": "score desc",
        "advtime": "",
        "advrange": "",
        "ext": "siteId:1862",
        "pNo": "1",
        "searchArea": "",
        "advtime": "",
        "advrange": "",
        "advepq": "",
        "advoq": "",
        "adveq": "",
        "searchArea": "",
        "advSiteArea": "",
        "q": "环境",
    }

    def edit_data(self, data: dict, keyword: str, page: int):
        data["q"] = keyword
        data["pNo"] = str(page)
        return data

    def edit_page(self, response):
        """解析总页数"""
        page = response.css("#panel-page > div > div.jcyh-lbys > div.default-result-list-paging > span > span::text").get()
        return int(page)

    def edit_items_box(self, response: Response):
        return response.css("div.default-result-list > div.searchMod")

    def edit_item(self, item):
        result = {}
        result["type"] = "unknown"
        result["title"] = item.css("div.news-style1 > h3>a::text").getall()
        result["url"] = item.css("div.news-style1 > h3 > a::attr(href)").get()
        result["date"] = item.css("p.dates >span::text").get()
        return result
