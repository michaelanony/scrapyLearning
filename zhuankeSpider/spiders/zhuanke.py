# -*- coding: utf-8 -*-

import scrapy
from zhuankeSpider.items import ZhuankespiderItem


class ZhuankeSpider(scrapy.Spider):
    name = 'zhuanke'
    allowed_domains = ['lanmaoyouhui.com']

    baseURL = "http://www.lanmaoyouhui.com/forum.php?mod=forumdisplay&fid=15&page="
    offset = 1
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        node_list = response.xpath("//div[@id='redtag']/a")
        # items=[]
        for node in node_list:
            item = ZhuankespiderItem()

            time = node.xpath("./span/text()").extract()
            title = node.xpath("./text()").extract()
            link = node.xpath("./@href").extract()

            item['time'] = time[0]
            item['title'] = title[0]
            item['link'] = "http://www.lanmaoyouhui.com/" + link[0]
            yield scrapy.Request(item['link'], meta={'item': item}, callback=self.parse1)
            # items.append(item)
            # 返回给管道处理
            yield item
        if self.offset < 1000:
            self.offset += 1
            url = self.baseURL + str(self.offset)
            yield scrapy.Request(url, callback=self.parse)
        # return items

    def parse1(self, response):
        item = response.meta['item']
        item['content'] = response.xpath("//div[@class='post-content']/p").extract()[0]
        return item
