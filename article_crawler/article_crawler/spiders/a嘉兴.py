from article_crawler.baseSpider import baseSpider


class a嘉兴Spider(baseSpider):
    name = '嘉兴'

    @baseSpider.parser('嘉兴', 'www.jiaxing.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#zoom  :not(script):not(style)::text').getall(),
        }
    @baseSpider.parser('嘉兴', 'www.jiaxing.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css(' div.content-text  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('嘉兴', 'www.jiaxing.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css('#ftcg  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('嘉兴', 'www.jiaxing.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css(' div.article-content-box  :not(script):not(style)::text').getall(),
        }