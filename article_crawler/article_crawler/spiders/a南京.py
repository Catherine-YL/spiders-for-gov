from article_crawler.baseSpider import baseSpider


class a南京Spider(baseSpider):
    name = '南京'

    @baseSpider.parser('南京', 'www.nanjing.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('body > div.main_content > div.main_content_right > div.main_content_p  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('南京', 'www.nanjing.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('div.main_content_p  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('南京', 'www.nanjing.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css('#con > div.view.TRS_UEDITOR.trs_paper_default.trs_word.trs_web  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('南京', 'www.nanjing.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css(
                'body > div.wrapper > div.content > div.detail_con > div.det_content > div  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('南京', 'www.nanjing.gov.cn')
    def parser_5(self, response, **kwargs):
        return {
            'content': response.css(
                'div.view.TRS_UEDITOR.trs_paper_default.trs_word  :not(script):not(style)::text').getall(),
        }

    @baseSpider.parser('南京', 'www.nanjing.gov.cn')
    def parser_6(self, response, **kwargs):
        return {
            'content': response.css(
                'div.view.TRS_UEDITOR.trs_paper_default.trs_web  :not(script):not(style)::text').getall(),
        }
    @baseSpider.parser('南京', 'www.nanjing.gov.cn')
    def parser_7(self, response, **kwargs):
        return {
            'content': response.css(
                'body :not(script):not(style)::text').getall(),
        }