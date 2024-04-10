# This interface implements the interaction with the website.
# It is the only part, where we actually scrape Google Scholar and get website content
# It is used by the ScholarScraper
# getURLRAWContent gets the content of a webpage as a raw HTML string

from abc import ABC, abstractmethod


class WebScraper(ABC):
    @abstractmethod
    def getURLRAWContent(self, title) -> str:
        ...

