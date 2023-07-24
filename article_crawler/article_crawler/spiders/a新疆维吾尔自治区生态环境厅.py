from article_crawler.baseSpider import baseSpider


class A新疆维吾尔自治区生态环境厅Spider(baseSpider):
    name = '新疆维吾尔自治区生态环境厅'

    @baseSpider.parser('新疆维吾尔自治区生态环境厅', 'sthjt.xinjiang.gov.cn')
    def parser_1(self, response, **kwargs):
        return {
            'content': response.css('#NewsContent  :not(script):not(style)::text').getall()
        }

    @baseSpider.parser('新疆维吾尔自治区生态环境厅', 'sthjt.xinjiang.gov.cn')
    def parser_2(self, response, **kwargs):
        return {
            'content': response.css('#gknbxq_box > div.gknbxq_detail  :not(script):not(style)::text').getall()
        }