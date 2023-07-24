from article_crawler.baseSpider import baseSpider


class A河南省生态环境厅Spider(baseSpider):
    name = '河南省生态环境厅'

    @baseSpider.parser('河南省生态环境厅', 'sthjt.henan.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#BodyLabel  :not(script):not(style)::text').getall(),
            'source': response.css('span.zw_sta  :not(script):not(style)::text').get()
        }#BodyLabel
