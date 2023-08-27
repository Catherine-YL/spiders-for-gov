from article_crawler.baseSpider import baseSpider


class A商丘Spider(baseSpider):
    name = '商丘'

    @baseSpider.parser('商丘', 'www.nanyang.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.conTxt :not(script):not(style)::text').getall(),
        }