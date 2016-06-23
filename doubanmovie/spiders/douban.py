# coding:utf-8
__author__ = 'LiangShuxian'

import re
import sys
from bs4 import BeautifulSoup
import scrapy
reload(sys)
# 使爬到的内容的编码是utf-8，默认是ascii
sys.setdefaultencoding('utf-8')


from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.http import Request
from scrapy.selector import Selector
sys.path.append('/Users/G_bgyl/douban/doubanmovie-master/doubanmovie/items.py ')
from doubanmovie.items import DoubanmovieItem


# count = 1

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
    num = 1
    nextLinks =[
        '?start=25&filter=',
        '?start=50&filter=',
        '?start=75&filter=',
        '?start=100&filter=',
        '?start=125&filter=',
        '?start=150&filter=',
        '?start=175&filter=',
        '?start=200&filter=',
        '?start=225&filter=',
    ]
    
    def parse(self, response):
        selector = Selector(response)
        Movies = selector.xpath('//div[@class="info"]')
        
        for eachMovie in Movies:
            movieurl = eachMovie.xpath('div[@class="hd"]/a/@href').extract()
            if movieurl:
                    # 变成str
                # self.count = selector.xpath('//div[@class="pic"]/em/text()').extract()
                movieurl = movieurl[0]
                yield Request(movieurl, callback=self.parse_info)

        # 抓取下一页，去掉这部分的注释，一次性抓取250个（其中有部分失效了，实际是245个）
        # nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        if self.num<=3:
            nextLink = self.nextLinks[self.num]
            self.num = self.num+1
            yield Request(self.url + nextLink, callback=self.parse)


        # if nextLink:
        #     nextLink = nextLink[0]
        #     print(nextLink)
        #     # 对下一页调用parse
        #     yield Request(self.url + nextLink, callback=self.parse)


    def parse_info(self,response):
        # count = self.count + 1
        item = DoubanmovieItem()
        selector1 = Selector(response)
            # 这里一定要记住加'//'
        title = selector1.xpath('//div[@id="content"]/h1/span[@property="v:itemreviewed"]/text()').extract()
        # director = selector1.xpath('//div[@id="info"]/span[1]/span[@class="attrs"]/a/text()').extract()
        # screenwriter = selector1.xpath('//div[@id="info"]/span[2]/span[@class="attrs"]/a/text()').extract()
        #
        # actor = selector1.xpath('//*[@id="info"]/span[@class="actor"]/span[@class="attrs"]/a/text()').extract()
        #
        # # // *[ @ id = "info"] / span[3] / span[2] / span[1] / a
        # # // *[ @ id = "info"] / span[3] / span[2] / span[2] / a
        # # //*[@id="info"]/span[3]/span[2]/span/a
        # # //*[@id="info"]/span[3]/span[2]/span[16]/a
        #
        # type = selector1.xpath('//div[@id="info"]/span[@property="v:genre"]/text()').extract()
        # #     # country和language都较难以获得，原因见豆瓣电影详情页面的网页html代码
        # #     # 错误： country = selector1.xpath('//div[@id="info"]/span[@class="pl"][2]')
        # mov_date = selector1.xpath('//div[@id="info"]/span[@property="v:initialReleaseDate"]/text()').extract()
        # if re.search('官方网站',response.body)!=None:
        #     mov_country = selector1.xpath('//span[@class="pl"]/following::text()[1]').extract()[5]
        #     # m2 = selector1.xpath('//span[@class="pl"]/text()').extract()[3]
        #     # m3 = selector1.xpath('//span[@class="pl"]/text()').extract()[4]
        #     # mov_country = [m1,m2,m3]
        #     mov_language = selector1.xpath('//span[@class="pl"]/following::text()[1]').extract()[6]
        #
        # else:
        #     mov_country = selector1.xpath('//span[@class="pl"]/following::text()[1]').extract()[4]
        #     mov_language = selector1.xpath('//span[@class="pl"]/following::text()[1]').extract()[5]
        #
        #
        #     # mov_country = response.body
        # # 以下代码希望能够匹配到span内容为"制片国家/地区"后的内容,但是"//span[./text()="\u5236\u7247\u56fd\u5bb6/\u5730\u533a\u003a")]"部分报错.
        # # mov_country = selector1.xpath('//span[./text()="\u5236\u7247\u56fd\u5bb6/\u5730\u533a\u003a")]/following::text()[1]').extract()
        # # contains(. / text(), "出版社:")
        # #mov_country0 = selector1.xpath('//*[@id="info"]/text()').extract()
        # # mov_country = re.match(r'\s*\w+', mov_country0)
        # mov_length = selector1.xpath('//div[@id="info"]/span[@property="v:runtime"]/@content').extract()
        # mov_introducton = selector1.xpath('//div[@id="link-report"]/span[2]/text()').extract()
        # if mov_introducton:
        #     mov_introducton = mov_introducton[0].strip()
        # else:
        #     mov_introducton = selector1.xpath('//div[@class="related-info"]/div[@class="indent"]/child::span[1]/text()').extract()
        #     mov_introducton = join(mov_introducton).strip()
        #
        # # //*[@id="info"]/span[6]
        rank = selector1.xpath('//div[@class="top250"]/span[@class="top250-no"]/text()').extract()
        # mov_score = selector1.xpath('//div[@typeof="v:Rating"]/strong[@property="v:average"]/text()').extract()
        # mov_image = selector1.select('//div[@id="mainpic"]/a[@class="nbgnbg"]/img/@src').extract()
        # mov_trailor = selector1.select('//div[@id="related-pic"]/ul/li/a[@class="related-pic-video"]/@href').extract()
        #
        # mov_pics = selector1.select('//div[@id="related-pic"]/ul/li/a/img/@src').extract()
        # if re.search('trailer',mov_pics[0])!=None:
        #     del mov_pics[0]
        # #     mov_pics1 = []
        # #     for i in mov_pics:
        # #         mov_pics1.append(i)
        # #     mov_pics = mov_pics1
        # # else:
        # #     mov_pics = mov_pics
        # # img[@alt="\u56fe\u7247"]/@src
        #
        # # mov_pics1 = []
        # # for pic in mov_pics:
        # #     pic = pic.replace('albumicon', 'photo')
        # #     mov_pics1.append(pic)
        # # mov_pics = mov_pics1
        # for i in range(len(mov_pics)):
        #     mov_pics[i] = mov_pics[i].replace('albumicon', 'photo')

        # [@class="related-pic-video"]
        item['rank'] = rank
        item['title'] = title
        # item['director'] = director
        # item['screenwriter'] = screenwriter
        # item['actor'] = actor
        # item['type'] = type
        # item['mov_date'] = mov_date
        # item['mov_country'] = mov_country
        # item['mov_length'] = mov_length
        # item['mov_introducton'] = mov_introducton
        # item['mov_score'] = mov_score
        # item['mov_image'] = mov_image
        # item['mov_language'] = mov_language
        # item['mov_trailor'] = mov_trailor
        # item['mov_pics'] = mov_pics



        yield item



def join(shuzu=['none','hi']):
    shuzu1 = ''
    for i in shuzu:
       shuzu1 = shuzu1+i
    return shuzu1





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





