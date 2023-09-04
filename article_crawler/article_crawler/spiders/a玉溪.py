from article_crawler.baseSpider import baseSpider


class A玉溪Spider(baseSpider):
    name = '玉溪'

    @baseSpider.parser('玉溪', 'www.yuxi.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            "content": response.css("div.content-txt p::text").getall(),
        }

    @baseSpider.parser('玉溪', 'mp.weixin.qq.com')
    def parser_2(self, response, **kwargs):
        return {
            "content": response.css("div.rich_media_content p::text").getall(),
        }

    @baseSpider.parser('玉溪', 'www.yuxi.gov.cn')
    def parser_3(self, response, **kwargs):
        return {
            "content": response.css("div.ArticleBody p::text").getall(),
        }

    @baseSpider.parser('玉溪', 'h.xinhuaxmt.com')
    def parser_4(self, response, **kwargs):
        return {
            "content": response.css("div section.main-text-container p::text").getall(),
        }
