# -*- coding: utf-8 -*-
import scrapy


class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["www.movie.douban.com"]
    start_urls = ['http://www.movie.douban.com/']

    def parse(self, response):

