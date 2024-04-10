import bs4
from bs4 import BeautifulSoup
import urllib.parse

from EasyScholar.Scraper.WebScraper.WebScraperSelenium import WebScraperSelenium


class ScholarScraper:

    def __init__(self, webscraper=None):
        if webscraper is None:
            webscraper = WebScraperSelenium()
        self.webscraper = webscraper

    @staticmethod
    def getURLFromTitle(title) -> str:
        title_safe = urllib.parse.quote_plus(title)
        url = "https://scholar.google.de/scholar?q=" + title_safe
        return url

    def getURLContent(self, url) -> bs4.BeautifulSoup:
        raw = self.webscraper.getURLRAWContent(url)
        print(raw)
        soup = BeautifulSoup(raw, "html.parser")
        return soup

    def getPublicationContent(self, title) -> bs4.BeautifulSoup:
        url = self.getURLFromTitle(title)
        content = self.getURLContent(url)
        return content
