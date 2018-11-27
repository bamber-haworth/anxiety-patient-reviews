import scrapy

class diazeSpider(scrapy.Spider):
    name = 'diazespider'
    start_urls = [
        "https://www.drugs.com/comments/diazepam/for-anxiety.html",
        "https://www.drugs.com/comments/diazepam/for-anxiety.html?page=2",
        "https://www.drugs.com/comments/diazepam/for-anxiety.html?page=3",
        "https://www.drugs.com/comments/diazepam/for-anxiety.html?page=4",
        "https://www.drugs.com/comments/diazepam/for-anxiety.html?page=5",
        "https://www.drugs.com/comments/diazepam/for-anxiety.html?page=6",
        "https://www.drugs.com/comments/diazepam/for-anxiety.html?page=7",
        "https://www.drugs.com/comments/diazepam/for-anxiety.html?page=8",
        "https://www.drugs.com/comments/diazepam/for-anxiety.html?page=9",
        "https://www.drugs.com/comments/diazepam/for-anxiety.html?page=10",
    ]

    def parse(self, response):
        for comment in response.xpath('//div[@class="user-comment"]'):
            yield {
                'text': comment.xpath('p/span/text()').extract(),
                #'score': comment.xpath('//div @class="rating-score"]/text()').extract()
            }