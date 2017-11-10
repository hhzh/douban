# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MovieItem(scrapy.Item):
    id = scrapy.Field()  # 条目id
    title = scrapy.Field()  # 中文名
    original_title = scrapy.Field()  # 原名
    aka = scrapy.Field()  # 又名
    alt = scrapy.Field()  # 条目页URL
    mobile_url = scrapy.Field()  # 移动版条目页URL
    rating = scrapy.Field()  # 评分
    ratings_count = scrapy.Field()  # 评分人数
    wish_count = scrapy.Field()  # 想看人数
    collect_count = scrapy.Field()  # 看过人数
    do_count = scrapy.Field()  # 在看人数
    images = scrapy.Field()  # 电影海报图
    subtype = scrapy.Field()  # 条目分类, movie或者tv
    directors = scrapy.Field()  # 导演
    casts = scrapy.Field()  # 主演
    writers = scrapy.Field()  # 编剧
    website = scrapy.Field()  # 官方网站
    douban_site = scrapy.Field()  # 豆瓣小站
    pubdates = scrapy.Field()  # 上映日期
    mainland_pubdate = scrapy.Field()  # 大陆上映日期
    year = scrapy.Field()  # 年代
    genres = scrapy.Field()  # 影片类型
    countries = scrapy.Field()  # 制片国家/地区
    languages = scrapy.Field()  # 语言
    release_date = scrapy.Field()  #
    durations = scrapy.Field()  # 片长
    summary = scrapy.Field()  # 简介
    comments_count = scrapy.Field()  # 短评数量
    reviews_count = scrapy.Field()  # 影评数量
    seasons_count = scrapy.Field()  # 总季数(tv only)
    current_season = scrapy.Field()  # 当前季数(tv only)
    episodes_count = scrapy.Field()  # 当前季的集数(tv only)
    schedule_url = scrapy.Field()  # 影讯页URL(movie only)
    trailer_urls = scrapy.Field()  # 预告片URL
    clip_urls = scrapy.Field()  # 片段URL
    blooper_urls = scrapy.Field()  # 花絮URL
    photos = scrapy.Field()  # 电影剧照
    popular_reviews = scrapy.Field()  # 影评
    imdb = scrapy.Field()  # IMDb链接
