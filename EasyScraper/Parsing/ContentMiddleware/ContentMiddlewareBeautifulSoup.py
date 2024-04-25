# Implements a scraping strategy for given Parsers
from bs4 import BeautifulSoup
from EasyScraper.Parsing.ContentMiddleware.ContentMiddleware import ContentMiddleware


class ContentMiddlewareBeautifulSoup(ContentMiddleware):

    def process(self, content):
        soup = BeautifulSoup(content, "html.parser")
        return soup
