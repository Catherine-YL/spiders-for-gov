from article_crawler.baseSpider import baseSpider


class A南阳Spider(baseSpider):
    name = '南阳'

    @baseSpider.parser('南阳', 'www.nanyang.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.article-box :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('南阳', 'www.nanyang.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.cont :not(script):not(style)::text').getall(),
        }