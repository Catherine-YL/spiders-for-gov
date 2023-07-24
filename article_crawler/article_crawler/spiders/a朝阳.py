from article_crawler.baseSpider import baseSpider


class A朝阳Spider(baseSpider):
    name = '朝阳'

    @baseSpider.parser('朝阳', 'www.chaoyang.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('body > div.main-wrap > div.wrap > div > div.center-info :not(script):not(style)::text').getall(),
            'source':response.css("body > div.fr  :not(script):not(style)::text").get()
        }

    @baseSpider.parser('朝阳', 'www.chaoyang.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('body > div.xiug-main > div.text  :not(script):not(style)::text').getall()

        }

    @baseSpider.parser('朝阳', 'www.chaoyang.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css('body > div.zhuant-warp > div > div > div.center-info  :not(script):not(style)::text').getall()
        }
    # def parser_5(self, response, **kwargs):
    #     return {
    #         'content': response.css('div.content  :not(script):not(style)::text').getall()
    #     }
