from article_crawler.baseSpider import baseSpider


class A滨州Spider(baseSpider):
    name = '滨州'

    @baseSpider.parser('滨州', 'www.binzhou.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.newsconParse p::text").getall()
        }

    @baseSpider.parser('滨州', 'www.binzhou.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("div table tr::text").getall()
        }

    @baseSpider.parser('滨州', 'www.binzhou.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css("div.newscontentpar p::text").getall()
        }

    @baseSpider.parser('滨州', 'www.binzhou.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css("div.newscontentpar span::text").getall()
        }

