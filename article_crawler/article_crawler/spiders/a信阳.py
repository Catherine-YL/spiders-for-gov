from article_crawler.baseSpider import baseSpider


class A信阳1pider(baseSpider):
    name = '信阳'

    @baseSpider.parser('信阳', 'www.xinyang.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#content  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('信阳', 'www.xinyang.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('div.word  :not(script):not(style)::text').getall(),
        }
