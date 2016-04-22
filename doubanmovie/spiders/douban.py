# coding:utf-8
__author__ = 'LiangShuxian'

import sys
reload(sys)
# 使爬到的内容的编码是utf-8，默认是ascii
sys.setdefaultencoding('utf-8')

import scrapy
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.http import Request
from scrapy.selector import Selector
from doubanmovie.items import DoubanmovieItem


# 抓top250项目
class doubanSpider(CrawlSpider):
    name = "douban"
    #    allowed_domains = ["oursim.whu.edu.cn"]
    #    start_urls = ["http://oursim.whu.edu.cn"]
    #
    #    url = 'https://oursim.whu.edu.cn'
    allowed_domains = ["movie.douban.com"]
    start_urls = ['https://movie.douban.com/top250']
    url = 'https://movie.douban.com/top250'
    
    def parse(self, response):
        selector = Selector(response)
        Movies = selector.xpath('//div[@class="info"]')
        
        for eachMovie in Movies:
            movieurl = eachMovie.xpath('div[@class="hd"]/a/@href').extract()
            if movieurl:
                # 变成str
                movieurl = movieurl[0]
                yield Request(movieurl, callback=self.parse_info)
        # 抓取下一页
#        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
#        if nextLink:
#            nextLink = nextLink[0]
#            print(nextLink)
#            # 对下一页调用parse
#            yield Request(self.url + nextLink, callback=self.parse)

    # 详细页面
    def parse_info(self,response):
        item = DoubanmovieItem()
        selector1 = Selector(response)
        # 这里一定要记住加'//'
        title = selector1.xpath('//div[@id="content"]/h1/span[@property="v:itemreviewed"]/text()').extract()
        director = selector1.xpath('//div[@id="info"]/span[1]/span[@class="attrs"]/a/text()').extract()
        screenwriter = selector1.xpath('//div[@id="info"]/span[2]/span[@class="attrs"]/a/text()').extract()
#        actor = selector1.xpath('//div[@id="info"]/span[@class="actor"]/span[@class="attrs"]/span/a/text()').extract()
        type = selector1.xpath('//div[@id="info"]/span[@property="v:genre"]/text()').extract()
        # country和language都较难以获得，原因见豆瓣电影详情页面的网页html代码
        # 错误： country = selector1.xpath('//div[@id="info"]/span[@class="pl"][2]')
        mov_date = selector1.xpath('//div[@id="info"]/span[@property="v:initialReleaseDate"]/text()').extract()
        mov_length = selector1.xpath('//div[@id="info"]/span[@property="v:runtime"]/@content').extract()
#        mov_introducton = selector1.xpath('//div[@class="related-info"]/div[@class="indent"]/span[@class="all hidden"]/text()')


        item['title'] = title
        item['director'] = director
        item['screenwriter'] = screenwriter
#        item['actor'] = actor
        item['type'] = type
        item['mov_date'] = mov_date
        item['mov_length'] = mov_length
#        item['mov_introducton'] = mov_introducton


        yield item









# 抓top250列表
#class doubanSpider(CrawlSpider):
#    name = "douban"
##    allowed_domains = ["oursim.whu.edu.cn"]
##    start_urls = ["http://oursim.whu.edu.cn"]
##    
##    url = 'https://oursim.whu.edu.cn'
#    allowed_domains = ["movie.douban.com"]
#    start_urls = ['https://movie.douban.com/top250']
#    url = 'https://movie.douban.com/top250'
#
#    def parse(self, response):
#        item = DoubanmovieItem()
#        selector = Selector(response)
##        news = selector.xpath('//div[@class="tm-list"]')
#        Movies = selector.xpath('//div[@class="info"]')
#        
#        for eachMovie in Movies:
#            title = eachMovie.xpath('div[@class="hd"]/a/span[@class="title"]/text()').extract()
##        for new in news:
##            title = new.xpath('ul/li/a/text()').extract()
#            movieurl = eachMovie.xpath('div[@class="hd"]/a/@href').extract()
#            
#            item['title'] = title
#            item['url'] = movieurl
#            yield item
#        # 抓取下一页
#        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
#        if nextLink:
#            nextLink = nextLink[0]
#            print(nextLink)
#            # 对下一页调用parse
#            yield Request(self.url + nextLink, callback=self.parse)
#            filename = response.url.split("/")[-2]
#            with open(filename, 'wb') as f:
#                f.write(self.url + nextLink +',')





