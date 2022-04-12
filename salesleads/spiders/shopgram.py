import scrapy
from scrapy_selenium import SeleniumRequest
from bs4 import BeautifulSoup


class ShopgramSpider(scrapy.Spider):
    name = 'shopgram'
    allowed_domains = ['https://trends.builtwith.com/']
    start_urls = ['https://trends.builtwith.com/websitelist/Shopify/Spain',
                  'https://trends.builtwith.com/websitelist/Shopify-Plus/Spain',
                  'https://trends.builtwith.com/websitelist/Magento/Spain',
                  'https://trends.builtwith.com/websitelist/WooCommerce-Checkout/Spain']

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        driver = response.request.meta['driver']
        soup = BeautifulSoup(driver.page_source, 'lxml')
        shop_urls = soup.findAll("tr", {"data-domain": True})
        for shop in shop_urls:
            item = {}
            td_list = shop.findAll("td")
            item['website'] = td_list[1].renderContents().decode("utf-8")
            item['location'] = td_list[2].renderContents().decode("utf-8").split(' ')[1]
            item['sales_revenue'] = td_list[3].renderContents().decode("utf-8")
            item['tech_spend'] = td_list[4].renderContents().decode("utf-8")
            item['social'] = td_list[5].renderContents().decode("utf-8")
            item['employees'] = td_list[6].renderContents().decode("utf-8")
            item['traffic'] = self.parse_traffic(td_list[7].renderContents().decode("utf-8"))
            yield item

    def parse_traffic(self, traffic):
        if traffic.lower() == "very high":
            return 3
        elif traffic.lower() == "high":
            return 2
        elif traffic.lower() == "medium":
            return 1
        else:
            return 0







