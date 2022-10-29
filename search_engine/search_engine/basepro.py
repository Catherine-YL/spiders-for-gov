import abc
import copy
import os
from typing import Any, Generator, Iterable, List, Optional, Union

import scrapy
from scrapy import FormRequest, Request
import termcolor
from search_engine.request import JsonRequest
from scrapy.shell import inspect_response
from scrapy.responsetypes import Response
from scrapy.utils import project
from scrapy.mail import MailSender
from termcolor import colored

from search_engine.extensions.keywords_reader import KeywordsReader


class ZhengFuBaseSpider(scrapy.Spider):
    name = ''
    start_urls = ['']
    # API
    api = ""
    # 模式 GET/POST
    method = "default"
    # 测试用 headers
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    cookie = ""
    # 数据模板
    data = {}
    # 是否解析第一页
    parse_first = True
    # 起始页api
    api_start: str = api
    # 起始页的索引 (某些情况下需要调整为 0 )
    start_page: int = 1
    # 启用关键词批量搜索
    batch: bool = False
    # debug
    debug: bool = False
    # start_mode
    start_mode = False
    # json_mode
    json_mode = False

    # 进度
    total_pages = 1 
    current_page = 0

    token_url = ''

    crawler_process = None

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.logger.debug(os.path.abspath(''))
        self.keywords = KeywordsReader()[self.name]
        self.mail = MailSender.from_settings(settings=project.get_project_settings())

    def start_requests(self) -> Generator[Union[Request, FormRequest], None, None]:
        """
        抛出初始请求
        """
        self.logger.debug("check keywords")
        keywords = self.keywords
        if not keywords:
            raise Exception("Need keywords!")

        self.logger.debug("check API")
        api = self.api
        if not api:
            raise Exception("Need API!")
        if self.cookie:
            self.headers['cookie'] = self.cookie

        self.logger.debug("check method")
        method = self.method
        if not method:
            raise Exception("Need method!")

        if self.batch:
            self.logger.debug("enable batch mode")

        yield from self.start_general_requests(method=method, page=self.start_page, callback=self.parse_index, start_mode=self.start_mode)

    def start_general_requests(self, method, page, callback, start_mode: bool =False, **kwargs):
        if method == "GET":
            general_method = self.start_get_requests
        elif method == "POST":
            general_method = self.start_post_requests
        else:
            raise Exception("Invalid method!")
        yield from general_method(page=page, callback=callback, start_mode=start_mode)

    def start_get_requests(self, page=None, callback=None, meta=None, start_mode=False, **kwargs) -> Generator[Request, None, None]:
        """抛出 GET 方法对应的起始请求."""
        keywords = self.keywords
        api = self.api_start if start_mode else self.api
        headers = self.headers
        if self.batch:
            # GET 方法不提供批量搜索
            pass
        else:
            for keyword in keywords:
                url = api.format(keyword=keyword, page=page)
                req = Request(url=url,
                              meta={"keyword": keyword},
                              headers=headers,
                              callback=callback)

                yield req

    def start_post_requests(self, page=1, callback=None, start_mode=False, **kwargs) -> Generator[Union[FormRequest, JsonRequest], None, None]:
        """抛出 POST 方法对应的起始请求."""
        keywords = self.keywords
        url = self.api_start if start_mode else self.api
        headers = self.headers
        self.logger.debug("爬取 第{}页".format(page))

        if self.json_mode:
            FormRequestCLS = JsonRequest
        else:
            FormRequestCLS = FormRequest

        if self.batch:
            keywords = self.keywords
            data = self.build_data(keywords, page, **kwargs)
            req = FormRequestCLS(
                url=url,
                meta={"keyword": keywords, "formdata": data, "page": page},
                headers=headers,
                formdata=data,
                callback=callback
            )
            yield req
        else:
            for keyword in keywords:
                data = self.build_data(keyword, page, **kwargs)
                req = FormRequestCLS(
                    url=url,
                    meta={"keyword": keyword, "formdata": data, "page": page},
                    headers=headers,
                    formdata=data,
                    callback=callback
                )
                yield req

    def parse_index(self, response: Response):
        """解析当前页，以及抛出余下请求."""
        self.current_page += 1
        percentage = float(self.current_page)/float(self.total_pages)
        self.logger.info(termcolor.colored(f"完成: {percentage}", "magenta"))

        parse_first = self.parse_first
        start_page = self.start_page

        ###########
        #  debug  #
        ###########
        if self.debug:
            self.debug = False
            inspect_response(response, self)
            self.crawler_process.stop()

        # 获取总页数
        total_page = min(self.edit_page(response), 500)
        self.total_pages += total_page
        self.logger.debug(
            colored("关键字[{}] 总页数: {}".format(response.meta.get('keyword'),
                                         total_page), "red"))

        end_page = start_page + total_page

        if parse_first:
            start_page += 1
            # 解析当前页
            yield from self.parse_items(response)

        # 抛出余下页的请求
        for page in range(start_page, end_page):
            yield from self.start_general_requests(method=self.method, 
                                                   page=page, 
                                                   callback=self.parse_items,
                                                   last_response=response)

    def build_data(self, keyword='煤炭', page=1, **kwargs):
        """从默认数据模板构造数据."""
        data = copy.copy(self.data)
        # 默认模板渲染
        data = self.render_data_template(data, keyword, page)
        # 开发接口
        data = self.edit_data(data, keyword, page, **kwargs)
        # 默认转换问字符串
        data = self.post_edit_data(data)
        return data

    def post_edit_data(self, data):
        for key, val in data.items():
            if val is None:
                continue
            data[key] = str(val)
        return data

    def render_data_template(self, data, keyword: str, page):
        for key, val in data.items():
            if '{page}' in str(val):
                data[key] = val.format(page=page)
            elif '{keyword}' in str(val):
                data[key] = val.format(keyword=keyword)
            elif '{keywords}' in str(val):
                data[key] = val.format(keywords=self.keywords)
        return data


    def parse_items(self, response):
        items_box = self.edit_items_box(response)
        items = self.edit_items(items_box)
        keyword = response.meta["keyword"]
        if not items:
            return
        for item in items:
            yield self.parse_item(item, keyword)

    def parse_item(self, item, keyword):
        """解析item"""
        item = self.edit_item(item)
        item = self.post_parse_item(item, keyword)
        if not item["url"]:
            return None
        return item

    def post_parse_item(self, item, keyword: str):
        """钩子函数，默认将关键字存入数据."""
        if not self.batch:
            item["keyword"] = keyword
        else:
            item['keyword'] = 'BATCH MODE'
            keywords = keyword
            for keyword in keywords:
                if keyword in item.get('title', '') or keyword in item.get('content', ''):
                    item['keyword'] = keyword
                    break

        # 添加城市名
        item['city'] = self.name

        # 处理item中列表
        for key, val in item.items():
            if isinstance(val, list):
                item[key] = ''.join(val)

        for key, val in item.items():
            if isinstance(val, str):
                item[key] = val.strip()

        return item

    def closed(self, reason):
        subject = 'scrapy report'
        body = """
        search_engine 蜘蛛 {0} 完成运行, 原因{1}.""".format(self.name, reason)
        return self.mail.send(to=["1070642565@qq.com"], subject=subject, body=body)

    ###############
    #  Interface  #
    ###############

    @abc.abstractmethod
    def edit_data(self, data: dict, keyword: str, page: int, **kwargs):
        """
        当请求方法为POST时应该发出的数据包
        input:
        data:dict
        return:
        data:dict
        kwagrs['last_response']
        """
        return data

    @abc.abstractmethod
    def edit_items_box(self, response: Response):
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def edit_items(self, items_box: Any):
        """
        从items容器中解析出items的迭代容器
        input: items_box
        return: items
        """
        return items_box

    @abc.abstractmethod
    def edit_item(self, item: Any):
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        return item

    @abc.abstractmethod
    def edit_page(self, response: Response) -> int:
        """
        input: response
        return: int
        """
        raise NotImplementedError()

