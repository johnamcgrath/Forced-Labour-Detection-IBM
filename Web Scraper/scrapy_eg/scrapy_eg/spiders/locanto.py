import datetime

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re


# run `scrapy crawl locanto_other2` in the Forced-Labour-Detection-IBM\Web Scraper\scrapy_eg\scrapy_eg\spiders> folder
# NOTE: delete csv file before running the spider
class LocantoSpider(CrawlSpider):
    name = "locanto"  # unique identifier for the spider
    # allowed_domains = ["www.locanto.ie"]  # limits the crawl to this domain list
    start_urls = ["https://www.locanto.ie/Customer-Service-Call-Centre/618/"]  # first url(s) to crawl
    # Crawling rules
    rules = (
        # use the parse() function on pages whose links match ".../ID_(number)/..." within the "entries" cs class
        # e.g. https://dublin.locanto.ie/ID_4964952094/Window-blinds-installer.html
        #       will match if it's in the list of entries on the page

        # get all jobs in this section. No locanto mobile pages or redirects.
        Rule(LinkExtractor(allow="locanto.ie/Customer-Service-Call-Centre/618/", deny=["m.locanto", "mobile_redirect"])),
        Rule(LinkExtractor(allow="locanto.ie/ID_", restrict_css=".entries"), callback="parse"),
    )

    def parse(self, response):
        title = response.css(".header-text::text").get()  # extract the title
        ad_id = response.css(".vap_ad_id::text").get()  # extract the ad id
        # format ad id
        ad_id = ad_id.replace("Ad ID: ", "")
        ad_id = ad_id.replace("\n", "")

        desc = response.xpath("//div[@itemprop='description']//text()").getall()  # extract the entire description
        desc = " ".join(desc)  # join the description into a single string
        desc = desc.replace("â€™", "\'")  # fix the unicode apostrophe, to be safe
        desc = re.sub("\s+", " ", desc)  # remove extra whitespace
        desc = desc.replace("About the Position", "")  # remove the About the Position text
        desc = desc.replace(" ", " ")  # remove the " " character
        desc = desc.encode("utf-8")  # convert to utf-8, just to be safe
        desc = desc.strip()  # remove leading and trailing whitespace

        # NOTE: NOT ALL ADS HAVE A USERNAME
        # username = response.css(".vap_sidebox_username::text").get()  # extract the username
        # username = username.replace("\n", "")  # format username

        # extract the location
        city = response.xpath("//div[@itemprop='address']/span[@itemprop='addressLocality']/text()").get()
        country = response.xpath("//div[@itemprop='address']/span[@itemprop='addressCountry']/text()").get()

        # extract ad sector
        breadcrumbs = response.xpath("//div[@class='breadcrumb_item']/a/text()").getall()
        length = len(breadcrumbs)
        sector = breadcrumbs[length-1]  # sector is the last breadcrumb on the ad page in locanto
        sector = sector.replace("\n", "")  # format sector
        sector = sector.rsplit(" ", 1)[0]  # remove the last word, which is just a location
        if "County" in sector:
            sector = sector.replace("County", "")  # remove the County from the sector
        if "Dún" in sector:
            sector = sector.replace("Dún", "")  # remove the Dún from the sector (e.g. if Dún Laoghaire is the location)
        sector = sector.strip()  # remove leading and trailing whitespace

        # NOTE: PHONE NUMBER REQUIRES A LOGGED IN ACCOUNT
        # NOTE: LOCANTO AD POSTED DATE IS RELATIVE TO TODAY'S DATE, NO SPECIFIC DATE (e.g. "Posted a week ago")
        yield {
            "title": title,
            "ad_id": ad_id,
            "desc": desc,
            "city": city,
            "country": country,
            "date": datetime.datetime.now().strftime("%Y-%m-%d"),  # placeholder date is of when the scraper is run
            "sector": sector
        }
