import scrapy
from search_engine.basepro import ZhengFuBaseSpider


class ChaoyangSpider(ZhengFuBaseSpider):
    """TODO SCRAPY"""
    name = '朝阳'
    allowed_domains = ['chaoyang.gov.cn']
    start_urls = ['http://www.chaoyang.gov.cn/']
    debug = False
    headers = {
        "Cookie":"c_search_key=%2C%2C%E4%BB%B7%E6%A0%BC; JSESSIONID=136B18BE516F54FF09C069DDA46F0AB2",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"
    }
    start_page = 0
    method = "POST"
    api = "http://www.chaoyang.gov.cn/search/search.ct"
    data = {
        'siteCode': 'CYSZF',
        'isAll': '0',
        'offset': "{page}",
        'limit': '20',
        'template': 'CYSZF',
        "resultOrderBy": "2",
        'ssfw': '2',
        'sswjlx': '1',
        'timefw': '1',
        'columnTypeId': '',
        'searchKey': '{keyword}',
    }
    def edit_data(self, data: dict, keyword: str, page: int) -> dict:
        """
        返回POST数据.
        """
        data["searchKey"] = keyword
        data["offset"] = str(page)
        return data

    def edit_items_box(self, response):
        return response.css(".result-li")

    def edit_item(self, item):
        result = {}
        result['url'] = item.css("a.tit::attr(href)").get()
        result['title'] = item.css("a.tit::text").getall()
        result['text'] = item.css("div.text::text").getall()
        result['date'] = item.css("div.time span::text").get()
        result['type'] = item.css("div.title div.lanm::text").get()
        return result

    def edit_page(self, response):
        try:
            return int(
                response.css(
                    "body > div.sousuo-wrap > div.ss-wrap.wrap-clear > div.left > div.fenye-wrap > span.nowpage::text"
                ).re(".*/(\d+)页")[0])
        except Exception:
            return 0
