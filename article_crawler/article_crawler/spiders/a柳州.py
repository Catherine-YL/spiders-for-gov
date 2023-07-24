from article_crawler.baseSpider import baseSpider


class a柳州Spider(baseSpider):
    name = '柳州'

    @baseSpider.parser('柳州', 'www.liuzhou.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.contentTextBox  :not(script):not(style)::text').getall(),
        }