from article_crawler.baseSpider import baseSpider


class A泰安Spider(baseSpider):
    name = '泰安'

    @baseSpider.parser('泰安', 'www.taian.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#zoom :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('泰安', 'www.taian.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#js_content :not(script):not(style)::text').getall(),
        }