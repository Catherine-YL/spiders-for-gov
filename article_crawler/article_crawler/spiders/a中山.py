from article_crawler.baseSpider import baseSpider


class A中山Spider(baseSpider):
    name = '中山'

    @baseSpider.parser('中山', 'www.huiyang.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.content p::text').getall(),
        }

    @baseSpider.parser('中山', 'www.shunde.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('div.article-content p::text').getall(),
        }

    @baseSpider.parser('中山', 'https://mp.weixin.qq.com')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css('div.rich_media_content p::text').getall(),
        }

    @baseSpider.parser('中山', 'www.gdqy.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css('div.article-content p::text').getall(),
        }

    @baseSpider.parser('中山', 'www.chaozhou.gov.cn')
    def parser_5(self, response, **kwargs):
        return {
            'content': response.css('div.detail_content p::text').getall(),
        }

    @baseSpider.parser('中山', 'www.gdnx.gov.cn')
    def parser_6(self, response, **kwargs):
        return {
            'content': response.css('div.article-content p::text').getall(),
        }

