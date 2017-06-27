# By: Ricky Morales
# Date: 4/27/2017
# This program uses Scrapy and Selenium to navigate to ESPN.com and
# scrape all the valuable information about each current UFC champ.

from selenium import webdriver
from scrapy.selector import Selector
from scrapy.item import Item, Field
from ufc_champions.items import UfcChampionsItem
import scrapy
import re
import time

class UFCchampionsSpider(scrapy.Spider):
    name = "current_champs"
    allowed_domains = ["espn.com"]
    start_urls = ["http://www.ufc.com/fighters"]

    def parse(self, response):

        items = []
        for sel in response.xpath('//*[@id="wc-title-holders"]'):
            item = UfcChampionsItem()
            item['flyweight'] = (sel.xpath('//*[@id="wc-title-holders"]/div/div/div[1]/text()').extract()[0] + ": " +
            sel.xpath('normalize-space(//*[@id="wc-title-holders"]/div/div/div[2]/div[1])').extract()[0] + " " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[2]/text()').extract()[0])

            item['bantamweight'] = (sel.xpath('//*[@id="wc-title-holders"]/div/div/div[1]/text()').extract()[1] + ": " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[1]/text()').extract()[1].strip() + " " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[2]/text()').extract()[1])

            item['featherweight'] = (sel.xpath('//*[@id="wc-title-holders"]/div/div/div[1]/text()').extract()[2] + ": " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[1]/text()').extract()[2].strip() + " " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[2]/text()').extract()[2])

            item['lightweight'] = (sel.xpath('//*[@id="wc-title-holders"]/div/div/div[1]/text()').extract()[3] + ": " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[1]/text()').extract()[3].strip() + " " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[2]/text()').extract()[3])

            item['welterweight'] = (sel.xpath('//*[@id="wc-title-holders"]/div/div/div[1]/text()').extract()[4] + ": " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[1]/text()').extract()[4].strip() + " " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[2]/text()').extract()[4])

            item['middleweight'] = (sel.xpath('//*[@id="wc-title-holders"]/div/div/div[1]/text()').extract()[5] + ": " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[1]/text()').extract()[5].strip() + " " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[2]/text()').extract()[5])

            item['lightheavyweight'] = (sel.xpath('//*[@id="wc-title-holders"]/div/div/div[1]/text()').extract()[6] + ": " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[1]/text()').extract()[6].strip() + " " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[2]/text()').extract()[6])

            item['heavyweight'] = (sel.xpath('//*[@id="wc-title-holders"]/div/div/div[1]/text()').extract()[7] + ": " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[1]/text()').extract()[7].strip() + " " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[2]/text()').extract()[7])

            item['wstrawweight'] = (sel.xpath('//*[@id="wc-title-holders"]/div/div/div[1]/text()').extract()[8] + ": " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[1]/text()').extract()[8].strip() + " " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[2]/text()').extract()[8])

            item['wbantamweight'] = (sel.xpath('//*[@id="wc-title-holders"]/div/div/div[1]/text()').extract()[9] + ": " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[1]/text()').extract()[9].strip() + " " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[2]/text()').extract()[9])

            item['wfeatherweight'] = (sel.xpath('//*[@id="wc-title-holders"]/div/div/div[1]/text()').extract()[10] + ": " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[1]/text()').extract()[10].strip() + " " +
            sel.xpath('//*[@id="wc-title-holders"]/div/div/div[2]/div[2]/text()').extract()[10])

            items.append(item)


        return items
