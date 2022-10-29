import scrapy
from search_engine.basepro import ZhengFuBaseSpider
from scrapy.selector import Selector


class YantaiSpider(ZhengFuBaseSpider):
    """TODO crawl"""
    name = '烟台'
    api = "http://www.yantai.gov.cn/jsearchfront/interfaces/cateSearch.do"
    method = "POST"
    data = {
        "websiteid": "370600000000000",
        "q": "{keyword}",
        "p": "{page}",
        "pg": "15",
        "cateid": "5",
        "pos": "",
        "pq": "",
        "oq": "",
        "eq": "",
        "begin": "",
        "end": "",
        "tpl": "82",
        "sortFields": ""
    }
    headers: dict[str, str] = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    debug = False

    def edit_items_box(self, response):
        raw_data = response.json()
        items_box = raw_data.get("result", None)
        return items_box

    def edit_items(self, items_box):
        items = [Selector(text=item, type="html") for item in items_box]
        return items

    def edit_item(self, item):
        data = {}
        data['title'] = item.css("div.jcse-news-title a::text").get()
        data['source'] = item.css("div.jcse-news-title > span > a::text").get()
        data['date'] = item.css("span.jcse-news-date::text").get()
        data['url'] = item.css("div.jcse-news-title a::attr(href)").get()
        return data

    def edit_page(self, response):
        raw_data = response.json()
        total_items_num = raw_data.get("total", 0)
        total_page_num = int(total_items_num) // 15 + 1
        return total_page_num
