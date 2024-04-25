# A middleware to preprocess content.
# This will be returned from a PageParser implementation. Giving it the right format
from abc import ABC, abstractmethod


class ContentMiddleware(ABC):

    @abstractmethod
    def process(self, content):
        pass
