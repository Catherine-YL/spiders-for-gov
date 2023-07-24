from article_crawler.baseSpider import baseSpider


class A株洲Spider(baseSpider):
    name = '株洲'

    @baseSpider.parser('株洲', 'www.zhuzhou.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.art_cont  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('株洲', 'www.zhuzhou.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#zoom  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('株洲', 'www.zhuzhou.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("div.article_bg  :not(script):not(style)::text").getall()
        }