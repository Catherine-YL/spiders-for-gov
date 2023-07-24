from article_crawler.baseSpider import baseSpider


class A济宁Spider(baseSpider):
    name = '济宁'

    @baseSpider.parser('济宁', 'www.jining.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#zoom  :not(script):not(style)::text').getall()
        }

    @baseSpider.parser('济宁', 'www.jining.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('# barrierfree_container > div.main  :not(script):not(style)::text').getall()

        }

    @baseSpider.parser('济宁', 'www.jining.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css('#barrierfree_container > div.main > div.main_content  :not(script):not(style)::text').getall()

        }

    @baseSpider.parser('济宁', 'www.jining.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css('# barrierfree_container > div.main.clearfix > div.main-right > div.content-box  :not(script):not(style)::text').getall()
        }

    @baseSpider.parser('济宁', 'www.jining.gov.cn')
    def parser_5(self, response, **kwargs):
        return {
            'content': response.css('div.content  :not(script):not(style)::text').getall()
        }
