Scrapes titles from a list of sites using Scrapy.  Add your domains to start_urls in /scraper/spiders/scrape.py

Usage (for JSON output to file titles.json):

scrapy crawl titleharvester --set FEED_URI=titles.json --set FEED_FORMAT=json

[{"title": ["Google"]},
{"title": ["Yahoo! UK"]}]

** other feed formats are XML or CSV.  Can extend with FEED_EXPORTERS http://doc.scrapy.org/topics/feed-exports.html