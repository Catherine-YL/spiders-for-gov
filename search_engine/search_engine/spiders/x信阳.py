from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector
import urllib
from urllib import parse

class X信阳Spider(ZhengFuBaseSpider):
    name = '信阳'
    api = "https://search1.henan.gov.cn/jrobot/search.do?_cus_lq_field_107=&_cus_eq_field_105=&_cus_eq_field_110=&_cus_pq_content=&_cus_eq_field_118=&_cus_eq_field_119=&_cus_eq_field_108=&_cus_eq_field_111=&_cus_eq_field_113=&_cus_eq_field_112=&webid=10047&pg=12&p={page}&tpl=&category=&_cus_query=&_cus_pq_content=&q={keyword}&pos=title&od=0&date=&date="
    method = "GET"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35",
        "Cookie": "_q=jiage%2Cjiage1%2C%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E8%A1%A2%E5%B7%9E%E5%B8%82%E7%94%9F%E6%80%81%E6%9C%8D%E5%8A%A1%E6%8B%9B%E5%95%86%E9%A1%B9%E7%9B%AE%E5%B9%B4%E5%AE%9E%E6%96%BD%E6%96%B9%E6%A1%88%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5%2C%E5%A4%A7%E5%9E%8B%E7%A7%91%E5%AD%A6%E4%BB%AA%E5%99%A8%E8%AE%BE%E5%A4%87%E5%8D%8F%E4%BD%9C%E5%85%B1%E4%BA%AB%2C%E5%AF%B9%E5%B0%86%E7%A6%81%E6%AD%A2%E6%88%96%E8%80%85%E9%99%90%E5%88%B6%E8%B0%83%E8%BF%90%E7%9A%84%E7%89%B9%E5%AE%9A%E5%8A%A8%E7%89%A9%E3%80%81%E5%8A%A8%E7%89%A9%E4%BA%A7%E5%93%81%E7%94%B1%E5%8A%A8%E7%89%A9%E7%96%AB%E7%97%85%E9%AB%98%E9%A3%8E%E9%99%A9%E5%8C%BA%E8%B0%83%E5%85%A5%E4%BD%8E%E9%A3%8E%E9%99%A9%E5%8C%BA%E7%9A%84%E8%A1%8C%E6%94%BF%E5%A4%84%E7%BD%9A%2C%E4%BB%B7%E6%A0%BC; user_sid=94e33a341a0b4e599dde82dbce18a830; JSESSIONID=DD7942B2C1BDAE919EEE8D7A8A58DB12; sid=ca3e646c6e3a03a4554d0d193075aa36; searchsign=36cf117578b944c48eb3e2d697639423; searchid=208ecc2fa5e74af58118e69d708d534b; zh_choose_undefined=s; ZJZWFWSESSIONID=9f0a29da-d1a9-4c58-9e63-c3aa718f4bf3; SERVERID=e5dad0f8f80595aa1b5885c8ed8d6944|1667792890|1667792881"
    }
    debug = False

    def edit_page(self, response: Response) -> int:
        pages = response.css("#jsearch-info-box::attr(data-total)").get()
        if pages == '':
            pages = 0
        else:
            pages = int(pages)//12+1
        return int(pages)

    def edit_items_box(self,response: Response) -> Selector:
        return response.css("#jsearch-result-items > div.jsearch-result-box")

    def edit_item(self,item)->dict:
        try:
            url= item.css("div.jsearch-result-title a::attr(href)").re('url=(.*)&q=')[0]
            url = str(url)
            new_txt = urllib.parse.unquote(url)

        except:
            new_txt = item.css("div.jsearch-result-title a::attr(href)").get()
        data = {
            'url':new_txt,
            'date':item.css("div.jsearch-result-abs-content span::text").get(),
            'source':"unknown",
            'type':"unknown",
            'title':item.css("div.jsearch-result-title a::text").getall()
        }
        return data

