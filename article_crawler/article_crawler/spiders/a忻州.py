from article_crawler.baseSpider import baseSpider


class A忻州Spider(baseSpider):
    name = '忻州'

    @baseSpider.parser('忻州', 'www.sxxz.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.article-body :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('忻州', 'www.sxxz.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.TRS_Editor :not(script):not(style)::text').getall(),
        }