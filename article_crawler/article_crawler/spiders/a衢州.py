from article_crawler.baseSpider import baseSpider


class A衢州Spider(baseSpider):
    name = '衢州'

    @baseSpider.parser('衢州', 'www.qz.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#zoom  :not(script):not(style)::text').getall(),
        }
