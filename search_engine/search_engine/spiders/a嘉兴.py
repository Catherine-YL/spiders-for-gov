import scrapy
from search_engine.basepro import ZhengFuBaseSpider
from scrapy.selector import Selector

import urllib
from urllib import parse
class JiaxingSpider(ZhengFuBaseSpider):
    """TODO crawl"""
    name = '嘉兴'
    api = "https://search.zj.gov.cn/jrobotfront/interfaces/cateSearch.do"
    headers = {
        "Cookie": " __jsluid_h=3934a1690556b58ff8921ccac8496085; __jsl_clearance=1667006408.782|0|Ubx5mnWnWkxA%2FoZ04bFQRycbBhI%3D; __jsluid_s=1880770df3ebf98ce094697511c99728; __jsl_clearance_s=1667006410.57|0|8iyLjAuamG0v9CEhPnQrmhUDEsU%3D; yfx_c_g_u_id_10006944=_ck22102909201513931517511749755; yfx_f_l_v_t_10006944=f_t_1667006415390__r_t_1667006415390__v_t_1667006415390__r_c_0; hefei_gova_SHIROJSESSIONID=af6e0615-828c-40b9-ac00-d7c3395f3a72",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"
    }
    method = "POST"
    start_urls = ['http://www.zj.gov.cn//']
    debug = False

    data = {
        "websiteid": "330401000000000",
        "pg": "10",
        "p": "{page}",
        "tpl": "2296",
        "Municipal_webid": "330401000000000",
        "Municipal_name": "嘉兴市",
        "isContains": "0",
        "q": "{keyword}",
        "cateid": "370",
        "sortType": "1",
        "pos": "filenumber,title,content,keyword",
    }

    def edit_items_box(self, response):
        return response.json().get('result')

    def edit_item(self, item):
        data = {}
        try:
            url = item.css("div.jcse-news-title > a::attr(href)").re('url=(.*)&q=')[0]
            url = str(url)
            new_txt = urllib.parse.unquote(url)
            data['url'] = new_txt
        except:
            data['url'] = item.css("div.jcse-news-title > a::attr(href)").get()
        data['type'] = item.css("span.typeTtitle > input.tagclass::attr(value)").get()
        data['title'] = item.css("div.jcse-news-title > a::text").getall()
        data['source'] = item.css("span.jcse-news-date.jcse-news-date2  ::text").getall()
        data['date'] = item.css("span.jcse-news-date.jcse-news-date1::text ").get()
        return data

    def edit_items(self, items_box):
        return [Selector(text=item) for item in items_box]

    def edit_page(self, response):
        raw_data = response.json()
        total_page_num = raw_data.get("total", 0)
        return int(total_page_num)//10+1

