from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scraper.items import ScraperItem

class ScraperSpider(BaseSpider):
	name = "titleharvester"
	start_urls = [
		"http://www.google.com",
		"http://www.yahoo.com"
	]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		sites = hxs.select('/html/head/title')
		items = []
		for site in sites:
			item = ScraperItem()
			item['title'] = site.select('text()').extract()
			items.append(item)
		return items
		


