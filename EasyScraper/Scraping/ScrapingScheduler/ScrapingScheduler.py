# Implements a scraping strategy for given Parsers
from abc import ABC, abstractmethod
from EasyScraper.Scraping.PageScraper.PageScraperSelenium import PageScraperSelenium


class ScrapingScheduler(ABC):

    def __init__(self, webscraper=None):
        if webscraper is None:
            webscraper = PageScraperSelenium()
        self.webscraper = webscraper

    def processParser(self, parser):
        url = parser.getURL()
        content = self.webscraper.getContent(url)
        for middleware in parser.getMiddlewares():
            content = middleware.process(content)
        parser.content = content

    @abstractmethod
    def scrape(self, parser):
        pass

