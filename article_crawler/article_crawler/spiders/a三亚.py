from article_crawler.baseSpider import baseSpider


class A三亚Spider(baseSpider):
    name = '三亚'

    @baseSpider.parser('三亚', 'www.sanya.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#UCAP-CONTENT  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('三亚', 'www.sanya.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('#news_content > ucapcontent  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('三亚', 'www.sanya.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css('#zoom  :not(script):not(style)::text').getall()
        }

    @baseSpider.parser('三亚', 'www.sanya.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css('#font-para  :not(script):not(style)::text').getall()
        }

    @baseSpider.parser('三亚', 'www.sanya.gov.cn')
    def parser_5(self, response, **kwargs):
        return {
            'content': response.css('div.content01  :not(script):not(style)::text').getall()
        }