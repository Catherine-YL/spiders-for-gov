from article_crawler.baseSpider import baseSpider


class A临沂Spider(baseSpider):
    name = '临沂'

    @baseSpider.parser('临沂', 'lyzwfw.sd.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#vbs_content_2  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('临沂', 'lyzwfw.sd.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("#js_content  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('临沂', 'lyzwfw.sd.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css("#vbs_content  :not(script):not(style)::text").getall()
        }
