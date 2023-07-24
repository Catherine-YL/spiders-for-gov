from article_crawler.baseSpider import baseSpider


class A湘潭Spider(baseSpider):
    name = '湘潭'

    @baseSpider.parser('湘潭', 'www.xiangtan.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.xl-xqnr  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('湘潭', 'www.xiangtan.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('#zoom  :not(script):not(style)::text').getall(),
        }

