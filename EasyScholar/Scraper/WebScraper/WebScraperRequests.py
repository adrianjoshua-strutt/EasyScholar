# This Scraper uses the standard requests class

import requests
from EasyScholar.Scraper.WebScraper.WebScraper import WebScraper

class WebScraperRequests(WebScraper):

    def getURLRAWContent(self, url) -> str:
        response = requests.get(url)
        return response.text
