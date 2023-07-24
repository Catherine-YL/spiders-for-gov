from article_crawler.baseSpider import baseSpider


class A淮北Spider(baseSpider):
    name = '淮北'

    @baseSpider.parser('淮北', 'www.huaibei.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css("#zoom  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('淮北', 'www.huaibei.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css("#J_content  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('淮北', 'www.huaibei.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            'content': response.css("div.wzcon  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('淮北', 'www.huaibei.gov.cn')
    def parser_4(self, response, **kwargs):
        return {
            'content': response.css("body > div > div.ls-page-container > div > div.ls-row.ls-article.clearfix > div > div.ls-article-info.j-fontContent  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('淮北', 'www.huaibei.gov.cn')
    def parser_5(self, response, **kwargs):
        return {
            'content': response.css("body > div > div.ls-page-container > div > div > div.ls-row.ls-article.clearfix > div > div.ls-article-info.min500.j-fontContent  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('淮北', 'www.huaibei.gov.cn')
    def parser_6(self, response, **kwargs):
        return {
            'content': response.css("body > div > div.ls-page-container > div > div > div.ls-row.ls-article.clearfix > div > div.ls-article-info.minh500.j-fontContent  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('淮北', 'www.huaibei.gov.cn')
    def parser_7(self, response, **kwargs):
        return {
            'content': response.css("body > div > div.ls-page-container.wza-region_main > div > div > div.ls-row.ls-article.clearfix > div > div.ls-article-info.j-fontContent  :not(script):not(style)::text").getall()
        }

    @baseSpider.parser('淮北', 'www.huaibei.gov.cn')
    def parser_7(self, response, **kwargs):
        return {
            'content': response.css(
                "body > div.wza-container.bodybg > div.container > div > div.con_main > div.con_mainline > div.j-fontContent.newscontnet.minh500  :not(script):not(style)::text").getall()
        }
