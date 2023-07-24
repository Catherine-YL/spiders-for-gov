from article_crawler.baseSpider import baseSpider


class A乌海Spider(baseSpider):
    name = '乌海'

    @baseSpider.parser('乌海', 'www.wuhai.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#zoom  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('乌海', 'www.wuhai.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('#wh_x_c  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('乌海', 'www.wuhai.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('body  :not(script):not(style)::text').getall(),
        }
