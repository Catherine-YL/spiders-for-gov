import scrapy
from search_engine.basepro import ZhengFuBaseSpider
from scrapy.selector import Selector


class J济南(ZhengFuBaseSpider):
    """TODO crawl"""
    name = '济南'
    api = "http://www.jinan.gov.cn/jsearchfront/interfaces/cateSearch.do"
    method = "POST"
    debug = True
    data = {
        "websiteid": "370100000000000",
        "q": "{keyword}",
        "p": "{page}",
        "pg": "10",
        "pos": "",
        "cateid": "1163",
        "tpl": "541"
    }
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    def edit_data(self, data, keyword, page):
        data["q"] = str(keyword)
        data["p"] = str(page)
        return data

    def edit_items_box(self, response):
        raw_data = response.json()
        items_box = raw_data["result"]
        return items_box

    def edit_items(self, items_box):
        items = [Selector(text=item, type="html") for item in items_box]
        return items

    def edit_item(self, item):
        data = {
            'url': item.css("div.jcse-news-url > a::text").get(),
            'title': item.css("div.jcse-news-title > a::text").getall(),
            'date': item.css("span.jcse-news-date::text").get()
        }
        return data

    def edit_page(self, response):
        raw_data = response.json()
        total_items_num = raw_data.get("total")
        total_page_num = int(total_items_num) // 10 + 1
        return total_page_num
