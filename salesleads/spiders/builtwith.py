import scrapy
from scrapy_selenium import SeleniumRequest
from bs4 import BeautifulSoup
from selenium import webdriver
from utils import get_start_urls


class BuildWithSpider(scrapy.Spider):
    name = 'buildwith'
    allowed_domains = ['trends.builtwith.com']
    start_urls = get_start_urls()

    def start_requests(self):
        """Call all the urls to scrap"""
        for url in self.start_urls:
            yield SeleniumRequest(url=url, wait_time=10, callback=self.parse)

    def parse(self, response):
        """Parse content to get sstores data"""
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
        """Parse traffic column to numerical value"""
        if traffic.lower() == "very high":
            return 3
        elif traffic.lower() == "high":
            return 2
        elif traffic.lower() == "medium":
            return 1
        else:
            return 0







