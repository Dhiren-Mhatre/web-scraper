import scrapy
import json

class NoberoSpider(scrapy.Spider):
    name = 'nobero'
    allowed_domains = ['nobero.com']
    start_urls = ['https://nobero.com/pages/men']

    def parse(self, response):
        categories = response.css('a.collection-grid-item__link::attr(href)').getall()
        for category in categories:
            yield response.follow(category, callback=self.parse_category)

    def parse_category(self, response):
        products = response.css('a.product-card__link::attr(href)').getall()
        for product in products:
            yield response.follow(product, callback=self.parse_product)

    def parse_product(self, response):
        item = {
            'category': response.css('nav.breadcrumb a:last-child::text').get(),
            'url': response.url,
            'title': response.css('h1.product-title::text').get().strip(),
            'price': int(response.css('span.price-item.price-item--sale::text').re_first(r'\d+')),
            'MRP': int(response.css('span.price-item.price-item--regular::text').re_first(r'\d+')),
            'last_7_day_sale': int(response.css('span.price-item.price-item--discounted::text').re_first(r'\d+')),
            'available_skus': self.parse_skus(response),
            'fit': self.get_feature(response, 'Fit'),
            'fabric': self.get_feature(response, 'Fabric'),
            'neck': self.get_feature(response, 'Neck'),
            'sleeve': self.get_feature(response, 'Sleeve'),
            'pattern': self.get_feature(response, 'Pattern'),
            'length': self.get_feature(response, 'Length'),
            'description': response.css('div.product-description div::text').getall()
        }
        yield item

    def parse_skus(self, response):
        skus = []
        colors = response.css('div.swatch__wrapper div::attr(data-swatch)').getall()
        sizes = response.css('div.variant-input-wrapper select option::text').getall()
        for color in colors:
            skus.append({
                'color': color,
                'size': sizes
            })
        return skus

    def get_feature(self, response, feature_name):
        return response.xpath(f'//span[contains(text(), "{feature_name}")]/following-sibling::span/text()').get().strip()
