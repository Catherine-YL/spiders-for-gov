from article_crawler.baseSpider import baseSpider


class A中山Spider(baseSpider):
    name = '中山'

    @baseSpider.parser('中山', 'www.zs.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.article  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('中山', 'www.zs.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css(' div.TRS_Editor  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('中山', 'www.zs.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css(' div.content  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('中山', 'www.zs.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.xxxq_text_cont  :not(script):not(style)::text').getall(),
        }