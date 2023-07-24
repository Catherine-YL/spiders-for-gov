from article_crawler.baseSpider import baseSpider


class A安徽省生态环境厅Spider(baseSpider):
    name = '安徽省生态环境厅'

    @baseSpider.parser('安徽省生态环境厅', 'sthjt.ah.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('div.j-fontContent.newscontnet.minh300  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('安徽省生态环境厅', 'sthjt.ah.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('div.message_con  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('安徽省生态环境厅', 'sthjt.ah.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css('div.j-fontContent.newscontnet.minh500  :not(script):not(style)::text').getall(),
        }