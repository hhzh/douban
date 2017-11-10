# -*- coding: utf-8 -*-
import scrapy
from douban.items import MovieItem
import re
from scrapy.http import Request
from urllib import parse


class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["movie.douban.com"]
    start_urls = ['https://movie.douban.com/subject/25790761/']

    def parse(self, response):
        item = MovieItem()
        id = response.xpath('//meta[@name="mobile-agent"]/@content').extract_first("")
        title = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract_first("")
        # original_title = response.xpath('').extract_first("")
        aka = response.xpath('//div[@id="info"]/text()[5]').extract_first("")
        # alt = response.xpath('').extract_first("")
        # mobile_url = response.xpath('').extract_first("")
        rating = response.xpath('//strong[contains(@class,"rating_num")]/text()').extract_first("")
        ratings_count = response.xpath('//a[@class="rating_people"]/span/text()').extract_first("")
        wish_count = response.xpath('//div[@class="subject-others-interests-ft"]/a[contains(@href,"/wishes")]/text()').extract_first("")
        collect_count = response.xpath('//div[@class="subject-others-interests-ft"]/a[contains(@href,"/collections")]/text()').extract_first("")
        # do_count = response.xpath('').extract_first("")
        images = response.xpath('//div[@id="mainpic"]/a/img/@src').extract_first("")
        # subtype = response.xpath('').extract_first("")
        directors = response.xpath('//div[@id="info"]/span/span[@class="attrs"]/a[@rel="v:directedBy"]/text()').extract()
        casts = response.xpath('//span[@class="actor"]/span[@class="attrs"]/span/a[@rel="v:starring"]/text()').extract()
        writers = response.xpath('//div[@id="info"]/span[2]/span[@class="attrs"]/a/text()').extract()
        # website = response.xpath('').extract_first("")
        # douban_site = response.xpath('').extract_first("")
        pubdates = response.xpath('//div[@id="info"]/span[@property="v:initialReleaseDate"]/text()').extract_first("")
        # mainland_pubdate = response.xpath('').extract_first("")
        year = response.xpath('//*[@id="content"]/h1/span[2]/text()').extract_first("")
        genres = response.xpath('//div[@id="info"]/span[@property="v:genre"]/text()').extract()
        # countries = response.xpath('').extract_first("")
        # languages = response.xpath('').extract_first("")
        # release_date = response.xpath('').extract_first("")
        durations = response.xpath('//div[@id="info"]/span[@property="v:runtime"]/text()').extract_first("")
        summary = response.xpath('//*[@id="link-report"]/span[@property="v:summary"]/text()').extract()
        comments_count = response.xpath('//*[@id="comments-section"]/div[@class="mod-hd"]/h2/span[@class="pl"]/a/@href').extract_first("")
        reviews_count = response.xpath('//*[@id="content"]/div/div/section/header/h2/span/a[@href="reviews"]/text()').extract_first("")
        # seasons_count = response.xpath('').extract_first("")
        # current_season = response.xpath('').extract_first("")
        # episodes_count = response.xpath('').extract_first("")
        # schedule_url = response.xpath('').extract_first("")
        trailer_urls = response.xpath('//*[@id="related-pic"]/ul/li[1]/a[@clas="related-pic-video"]/@href').extract_first("")
        # clip_urls = response.xpath('').extract_first("")
        # blooper_urls = response.xpath('').extract_first("")
        photos = response.xpath('//*[@id="related-pic"]/ul/li[2]/a/img[@alt="图片"]/@src').extract()
        popular_reviews = response.xpath('//*[@id="hot-comments"]/div[1]/div/p/text()').extract_first("")

        id_match_re = re.match('.*com/movie/subject/(\d+)/.*', id)
        id_content = 0
        if id_match_re:
            id_content = int(id_match_re.group(1))
        item['id'] = id_content
        item['title'] = title
        item['aka'] = aka
        item['rating'] = rating
        item['ratings_count'] = ratings_count
        item['wish_count'] = wish_count
        item['collect_count'] = collect_count
        item['images'] = images
        item['directors'] = '/'.join(directors)
        item['casts'] = '/'.join(casts)
        item['writers'] = '/'.join(writers)
        item['pubdates'] = pubdates
        item['year'] = year
        item['genres'] = '/'.join(genres)
        item['durations'] = durations
        item['summary'] = '/'.join(summary)
        item['comments_count'] = comments_count
        item['reviews_count'] = reviews_count
        item['trailer_urls'] = trailer_urls
        item['photos'] = '/'.join(photos)
        item['popular_reviews'] = popular_reviews

        yield item

        next_urls = response.xpath('//div[@id="recommendations"]/div[@class="recommendations-bd"]/dl/dt/a/@href').extract()
        for next_url in next_urls:
            print('next_url:%s' % next_url)
            yield Request(url=next_url, callback=self.parse)
