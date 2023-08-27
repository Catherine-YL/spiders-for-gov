from article_crawler.baseSpider import baseSpider


class A长沙Spider(baseSpider):
    name = "长沙"

    @baseSpider.parser('长沙', 'www.changsha.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#zoom  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('长沙', 'www.changsha.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('div.pages_content.TRS_Editor  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('长沙', 'www.changsha.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css('div.content-main  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('长沙', 'www.changsha.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css('div.ue_table  :not(script):not(style)::text').getall(),
        }


    @baseSpider.parser('长沙', 'www.changsha.gov.cn')
    def parser_5(self, response, **kwargs):
        return {
            'content': response.css('div.czys_datail_content  :not(script):not(style)::text').getall(),
        }