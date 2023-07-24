from article_crawler.baseSpider import baseSpider


class A黑龙江省生态环境厅Spider(baseSpider):
    name = '黑龙江省生态环境厅'

    @baseSpider.parser('黑龙江省生态环境厅', 'http://221.212.115.3:8888/')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.content  :not(script):not(style)::text').getall(),
        }