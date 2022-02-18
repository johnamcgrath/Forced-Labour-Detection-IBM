import scrapy


class LocantoOtherSpider(scrapy.Spider):
    name = "locanto_other"  # unique identifier for the spider
    allowed_domains = ["www.locanto.ie/Other-Jobs/615"]  # limits the crawl to this domain list
    start_urls = ["https://www.locanto.ie/Other-Jobs/615/"]  # first url to crawl

    def parse(self, response):
        # Extract content using css selectors
        titles = response.css(".bp_ad__title_link::text").getall()
        locations = response.css(".bp_ad__city::text").getall()
        shortdesc = response.css(".bp_ad__desc_link::text").getall()

        # Give the extracted content row wise
        for item in zip(titles, locations, shortdesc):
            # create a dictionary to store the scraped info
            scraped_info = {
                "title": item[0],
                "location": item[1],
                "shortdesc": item[2],
            }

            # yield (give) the scraped info to scrapy, which deals with it as in settings.py
            yield scraped_info
