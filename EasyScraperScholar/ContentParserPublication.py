import bs4
from EasyScraper.Parsing.ContentMiddleware.ContentMiddleware import ContentMiddleware
from EasyScraper.Parsing.ContentMiddleware.ContentMiddlewareBeautifulSoup import ContentMiddlewareBeautifulSoup
from EasyScraper.Parsing.ContentParser.ContentParser import ContentParser
import urllib.parse
from html import unescape


class ContentParserPublication(ContentParser):

    def getMiddlewares(self) -> [ContentMiddleware]:
        return [ContentMiddlewareBeautifulSoup()]

    def getURL(self) -> str:
        title_safe = urllib.parse.quote_plus(self.query)
        url = "https://scholar.google.de/scholar?q=" + title_safe
        return url

    def isContentAvailable(self) -> bool:
        return str(self.content) != "" and "gs_captcha_f" not in str(self.content)

    def getTitleHref(self) -> bs4.BeautifulSoup:
        return self.content.find_all(lambda tag: tag.name == "a" and self.query in tag.text)[0]

    def parsePublicationURL(self) -> str:
        return self.getTitleHref()['href']

    def parseDataCID(self) -> str:
        return self.getTitleHref()['data-clk-atid']

    def parseTagLine(self) -> str:
        return unescape(str(self.getTitleHref().parent.findNext('div').contents[0])).replace("\xa0", " ")
