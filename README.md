# scrapy
Commands:

response.css("title::text").extract()[0]

response.css("title::text").extract_first()


response.xpath('//title/text()').extract_first() 



Multiple Selector:
"div.tags a.tag::text"
