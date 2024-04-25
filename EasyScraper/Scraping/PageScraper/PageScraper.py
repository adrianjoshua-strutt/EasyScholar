# This interface implements the interaction with the website.
# Given a URL it returns its HTML content
# It is the only part, where we actually scrape the url and get websites content
# getURLRAWContent returns the content of a webpage as a raw HTML string

from abc import ABC, abstractmethod


class PageScraper(ABC):
    @abstractmethod
    def getContent(self, url) -> str:
        """
        Given a URL returns its HTML content
        :return: The raw website content
        """

