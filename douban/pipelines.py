# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from douban.items import MovieItem


class DoubanPipeline(object):
    def __init__(self):
        self.ids = set()

    def process_item(self, item, spider):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='SCMD_2017_scmd', db='douban',
                               charset='utf8')
        cursor = conn.cursor()
        try:
            if item['id'] in self.ids:
                print("Duplicate id found: %s" % item[id])
            else:
                sql = 'insert into movie (id,title,aka,rating,ratings_count,wish_count,collect_count,images,directors,' \
                      'casts,writers,pubdates, year,genres,durations,summary,comments_count,reviews_count,trailer_urls,' \
                      'photos,popular_reviews) ' \
                      'values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                exec_result = cursor.execute(sql,
                                             (item['id'], item['title'], item['aka'], item['rating'],
                                              item['ratings_count'], item['wish_count'], item['collect_count'],
                                              item['images'], item['directors'], item['casts'], item['writers'],
                                              item['pubdates'], item['year'], item['genres'], item['durations'],
                                              item['summary'], item['comments_count'], item['reviews_count'],
                                              item['trailer_urls'], item['photos'], item['popular_reviews']))
                conn.commit()
        except Exception as e:
            print('insert error:%s' % item['id'])
            print(e)
        conn.close()
        return item
