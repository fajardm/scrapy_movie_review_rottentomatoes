# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    release_date = scrapy.Field()
    review_list = scrapy.Field()
    pass


class ReviewItem(scrapy.Item):
    name = scrapy.Field()
    review_date = scrapy.Field()
    review_desc = scrapy.Field()
    pass
