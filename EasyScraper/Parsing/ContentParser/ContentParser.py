# Given the Sourcecode of a page this module will return selected attributes
# Implementing attribute methods should start with "parse" e.g. "parsePageTitle(self)"
import warnings
from abc import ABC, abstractmethod

from EasyScraper.Parsing.ContentMiddleware.ContentMiddleware import ContentMiddleware


class ContentParser(ABC):

    def __init__(self, query, content=None):
        self.query = query
        self.content = content

    @abstractmethod
    def getURL(self) -> str:
        """
        Returns the corresponding URL to scrape depending on the query
        :return: The URL to scrape
        """
        pass

    @abstractmethod
    def isContentAvailable(self) -> bool:
        """
        Returns, whether the request got blocked. Is necessary for the ScrapingScheduler.
        E.g. checks for CAPTCHA prompts.
        :return: If content is available for parsing.
        """
        pass

    @abstractmethod
    def getMiddlewares(self) -> [ContentMiddleware]:
        """
        Returns, content Middlewares to apply to RAW content
        :return List of ContentMiddlewares
        """
        pass

    def toDict(self) -> dict:
        if self.content is None:
            warnings.warn("toDict on ContentParser with empty content")
            return {}
        elif self.isContentAvailable() is False:
            warnings.warn("toDict on ContentParser with isAvailable FALSE")
            return {}
        methods = [method for method in dir(self) if callable(getattr(self, method)) and method.startswith('parse')]
        return {method[5:]: getattr(self, method)() for method in methods}

    def __str__(self) -> str:
        return self.toDict().__str__()
