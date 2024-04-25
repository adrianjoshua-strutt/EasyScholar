# This Scraper uses the standard requests class
import requests
from EasyScraper.Scraping.PageScraper.PageScraper import PageScraper


class PageScraperRequests(PageScraper):

    def getContent(self, url) -> str:
        response = requests.get(url)
        return response.text
