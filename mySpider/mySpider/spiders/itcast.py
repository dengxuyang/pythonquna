import scrapy
from mySpider.items import ItcastItem
import json


class Opp2Spider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.com']
    start_urls = ("https://touch.qunar.com/hotelcn/api/hotellist", )

    def start_requests(self):
        # for url in self.start_urls:
        #     yield scrapy.Request(url,callback=self.parse)
        print('start_requests()')
        # post请求的参数
        data = {
            "city": "杭州",
            "cityUrl": "hangzhou",
            "checkInDate": "2021-05-16",
            "checkOutDate": "2021-05-17",
            "page": 1,
        }
        for url in self.start_urls:
            yield scrapy.Request(url, body=json.dumps(data), method='POST', headers={'Content-Type': 'application/json'})

    def parse(self, response):
        #open("teacher.html","wb").write(response.body).close()

        # 存放老师信息的集合
        items = []

        # for each in response.xpath("//div[@class='li_txt']"):
        #     # 将我们得到的数据封装到一个 `ItcastItem` 对象
        #     item = ItcastItem()
        #     #extract()方法返回的都是unicode字符串
        #     name = each.xpath("h3/text()").extract()
        #     title = each.xpath("h4/text()").extract()
        #     info = each.xpath("p/text()").extract()

        #     #xpath返回的是包含一个元素的列表
        #     item['name'] = name[0]
        #     item['title'] = title[0]
        #     item['info'] = info[0]

        #     items.append(item)
        # 直接返回最后数据
        # {b'Content-Length': b'22', b'Date': b'Sun, 16 May 2021 10:30:26 GMT', b'Content-Type': b'application/json; charset=utf-8', b'Set-Cookie': b'HN2=quqlsrkssqucs; Max-Age=2592000; Domain=qunar.com; Path=/; Expires=Tue, 15 Jun 2021 10:30:26 GMT', b'Etag': b'W/"16-FE22scPRpI3yzR01v7+laHJEeS0"', b'Server': b'QWS/1.0', b'Req-Id': b'00006600075832bbd210b2a3'}
        print(response.text)
        return items