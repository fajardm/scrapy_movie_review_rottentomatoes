import scrapy
from scrapy.spiders import SitemapSpider
from scrapy_comment.items import MovieItem, ReviewItem


class RottenSpider(SitemapSpider):
    name = 'rotten'
    allowed_domains = ['rottentomatoes.com']
    sitemap_urls = ['https://www.rottentomatoes.com/sitemap.xml']
    sitemap_rules = [('/m/', 'parse_movie')]
    movie = None

    def parse_movie(self, response):
        critic_headers = response.css("p#criticHeaders a::attr(href)").extract_first()

        if critic_headers is not None:
            title = response.css('meta[name="movieTitle"]::attr(content)').extract_first(default='').strip()

            if title != '':
                self.movie = MovieItem(title=title)
                return scrapy.Request('https://www.rottentomatoes.com' + critic_headers, self.parse_review)

        pass

    def parse_review(self, response):
        rows = response.css("div.review_table > div.review_table_row")

        reviews = []

        for row in rows:
            name = row.css("div.col-xs-8 div.critic_name a::text").extract_first(default='').strip()
            review_desc = row.css("div.review_container div.the_review::text").extract_first(default='').strip()
            review_date = row.css("div.review_container div.review_date::text").extract_first(default='').strip()

            if name != '' and review_desc != '':
                review = ReviewItem(name=name, review_date=review_date, review_desc=review_desc)
                reviews.append(review)

        self.movie['review_list'] = reviews

        self.logger.info('RESULT 3 %s', self.movie)

        yield self.movie
