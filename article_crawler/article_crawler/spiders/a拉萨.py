from article_crawler.baseSpider import baseSpider


class a拉萨Spider(baseSpider):
    name = '拉萨'

    @baseSpider.parser('拉萨', 'www.lasa.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#NewsContent  :not(script):not(style)::text').getall(),
        }