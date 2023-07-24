from article_crawler.baseSpider import baseSpider


class A三明Spider(baseSpider):
    name = '三明'

    @baseSpider.parser('三明', 'www.sm.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.TRS_Editor  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('三明', 'www.sm.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css(' #detailCont  :not(script):not(style)::text').getall(),
        }
