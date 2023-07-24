from article_crawler.baseSpider import baseSpider


class a金华Spider(baseSpider):
    name = '金华'

    @baseSpider.parser('金华', 'www.jinhua.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#mainText  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('金华', 'www.jinhua.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css(' div.jh_xl_m2  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('金华', 'www.jinhua.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css('#zoom  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('金华', 'www.jinhua.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css('#contentText  :not(script):not(style)::text').getall(),
        }