import scrapy
from search_engine.basepro import ZhengFuBaseSpider


class ZhongshanSpider(ZhengFuBaseSpider):
    """TODO crawl"""
    name = '中山'
    # allowed_domains = ['zs.gov.cn', 'gd.gov.cn']
    api = "http://search.gd.gov.cn/api/search/all"
    method = "POST"
    data = {
        "gdbsDivision": "442000",
        "keywords": "{keyword}",
        "page": "{page}",
        "position": "title",
        "range": "site",
        "recommand": "1",
        "service_area": "760",
        "site_id": "760001",
        "sort": "smart"
    }

    def edit_data(self, data, keyword, page):
        data["keywords"] = str(keyword)
        data["page"] = str(page)
        return data

    def edit_page(self, response):
        raw_data = response.json()
        total_items_num = raw_data["data"]["news"]["total"]
        total_page_num = int(total_items_num) // 20 + 1
        return total_page_num

    def edit_items_box(self, response):
        raw_data = response.json()
        items_box = raw_data["data"]["news"]["list"]
        return items_box

    def edit_item(self, item):
        data = {
            'url': item['url'],
            'title': scrapy.Selector(text=item['title']).css('::text').getall(),
            'date': item['pub_time'],
            'source': item['source'],
        }
        return data
