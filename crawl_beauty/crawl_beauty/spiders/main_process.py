import scrapy
from crawl_beauty.items import CrawlBeautyItem

class BeautySpider(scrapy.Spider):
    name = "crawl_beauty"
    allowed_domains = ["www.win4000.com"]
    start_urls = ['http://www.win4000.com/zt/bijini.html',
                  # 'http://www.mm131.com/qingchun/',
                  # 'http://www.mm131.com/xiaohua/',
                  # 'http://www.mm131.com/chemo/',
                  # 'http://www.mm131.com/qipao/',
                  # 'http://www.mm131.com/mingxing/'
                  ]

    def parse(self, response):
        list = response.css(".clearfix ul")
        for img in list:
            imgurl = img.css("a::attr(href)").extract()
            print(imgurl)

    # def content(self, response):
    #     item = CrawlBeautyItem()
    #     item['name'] = response.css(".content h5::text").extract_first()
    #     item['ImgUrl'] = response.css(".content-pic img::attr(src)").extract()
    #     yield item
    #     # 提取图片,存入文件夹
    #     # print(item['ImgUrl'])
    #     next_url = response.css(".page-ch:last-child::attr(href)").extract_first()
    #
    #     if next_url is not None:
    #         # 下一页
    #         yield response.follow(next_url, callback=self.content)