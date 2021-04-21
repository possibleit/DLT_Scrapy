import scrapy
from scrapy import Request

from tutorial.items import TutorialItem, item
from tutorial.utils import save2file, _save2file


class QuotesSpider(scrapy.Spider):
    name = "quotes"  # yinli

    def start_requests(self):
        urls = [
            'http://www.bzmfxz.com/biaozhun/Soft/DLDLBZ/List_1.html',
        ]
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):

        ''''
        response是获取到的html文档
        //*[@id="main_right_box"]/div[2]/div[3]/div/div 选取到cmainbox属性的div
        '''
        time = response.xpath('//*[@id="main_right_box"]/div[2]/div[3]/div/div/div[@class="childclasslist_time"]/text()').extract()
        DLT = response.xpath('//*[@id="main_right_box"]/div[2]/div[3]/div/div/a[@target="_blank"]/text()').extract()
        link = response.xpath('//*[@id="pe100_page_infolist"]/a[last()-1]/@href')[0].extract()

        T = TutorialItem()
        T['url_nxt'] = link
        for i, j in zip(time, DLT):
            T.item[j] = i
        yield T
        next_url = "http://www.bzmfxz.com/" + T['url_nxt']
        yield Request(next_url)
