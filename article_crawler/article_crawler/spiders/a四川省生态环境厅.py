from article_crawler.baseSpider import baseSpider


class A四川省生态环境厅Spider(baseSpider):
    name = '四川省生态环境厅'

    @baseSpider.parser('四川省生态环境厅', 'sthjt.sc.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.TRS_Editor  :not(script):not(style)::text').getall()
        }

    @baseSpider.parser('四川省生态环境厅', 'sthjt.sc.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('div.nrcontent  :not(script):not(style)::text').getall()
        }

    @baseSpider.parser('四川省生态环境厅', 'sthjt.sc.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css('div.content  :not(script):not(style)::text').getall()
        }

    @baseSpider.parser('四川省生态环境厅', 'sthjt.sc.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css('div.xl_cont  :not(script):not(style)::text').getall()
        }