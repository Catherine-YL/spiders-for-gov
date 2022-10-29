import scrapy
from search_engine.basepro import ZhengFuBaseSpider


class H淮北(ZhengFuBaseSpider):
    name = '淮北'
    allowed_domains = ['www.huaibei.gov.cn']
    start_urls = ['http://http://www.huaibei.gov.cn//']
    api = "https://www.huaibei.gov.cn/site/tpl/3361?isAllSite=true&platformCode=&siteId=&columnId=&columnIds=&typeCode=articleNews,pictureNews,videoNews,policyDoc,explainDoc&beginDate=&endDate=&fromCode=&keywords={keyword}&excColumns=&datecode=&sort=intelligent&type=&tableColumnId=&subkeywords={keyword}&orderType=0&indexNum=&fileNum=&pid=&language=&flag=false&searchType=&searchTplId=&fuzzySearch=true&internalCall=&catIds=&colloquial=true&pageIndex={page}&pageSize=10"

    method = "GET"

    def edit_page(self, response):
        total_items = response.css("div.searchType-column > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > span:nth-child(1)::text").get()
        total_page = int(total_items) // 10 + 1
        return total_page

    def edit_items_box(self, response):
        items_box = response.css("div#search_list")
        return items_box

    def edit_items(self, items_box):
        items = items_box.css("ul.search-list")
        return items

    def edit_item(self, item):
        data = {
            'url':item.css("li.search-title > a::attr(href)").get(),
            'title': item.css("li.search-title > a::attr(title)").get(),
            'type': item.css("li.search-title > span::text").get(),
            'source':item.css("li.search-resources > span.author::text").get(),
            'date':item.css("li.search-resources > span.date::text").get()
        }
        return data
