from article_crawler.baseSpider import baseSpider


class A运城Spider(baseSpider):
    name = "运城"

    @baseSpider.parser('运城', 'www.yuncheng.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#UCAP-CONTENT  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('运城', 'www.yuncheng.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('#info_content  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('运城', 'www.yuncheng.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css('div.art-con.art-con-bottonmLine  :not(script):not(style)::text').getall(),
        }