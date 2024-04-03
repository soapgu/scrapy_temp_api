import scrapy
import chompjs


class MySpider(scrapy.Spider):
    name = "temp_api"
    start_urls = [
        "http://sh.weather.com.cn/",
    ]

    def parse(self, response):
        next_url = response.css('script[src*=sk_2d]').attrib["src"]
        self.log(next_url)
        headers = {'Referer':'http://sh.weather.com.cn/'}
        yield scrapy.Request(next_url, callback=self.parse_script,headers=headers) 
    
    def parse_script(self,response):
        data = chompjs.parse_js_object(response.body.decode('utf-8'))
        yield data