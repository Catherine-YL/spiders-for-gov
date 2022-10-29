import scrapy
from search_engine.basepro import ZhengFuBaseSpider


class HuangshanSpider(ZhengFuBaseSpider):
    """TODO crawl"""
    name = '黄山'
    allowed_domains = ['huangshan.gov.cn']
    api = "http://www.huangshan.gov.cn/site/label/8888?IsAjax=1&dataType=JSON&labelName=searchDataList&fuzzySearch=false&level=&fromCode=title&showType=2&titleLength=35&contentLength=100&islight=true&isJson=true&pageSize=10&pageIndex={page}&isForPage=true&sort=desc&datecode=&typeCode=all&siteId=6793336&columnId=&platformCode=huangshan_ex9_1&isAllSite=true&isForNum=true&beginDate=&endDate=&keywords={keyword}&subkeywords=&isAttach=1&orderType=1"
    method = "GET"

    def edit_items_box(self, response):
        raw_data = response.json()
        items_box = raw_data['data']['data']
        return items_box

    def edit_item(self, item):
        item_data = {
            'url': item['link'],
            'title': scrapy.Selector(text=item['title']).css("::text").getall(),
            'source': item['resources'],
            'date': item['createDate'],
        }
        return item_data

    def edit_page(self, response):
        raw_data = response.json()
        total_page = raw_data['data']['pageCount']
        return int(total_page)

