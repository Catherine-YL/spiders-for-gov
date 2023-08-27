from article_crawler.baseSpider import baseSpider


class A许昌Spider(baseSpider):
    name = '许昌'

    @baseSpider.parser('许昌', 'www.taian.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#zoom :not(script):not(style)::text').getall(),
        }