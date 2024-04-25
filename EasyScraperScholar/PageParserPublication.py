from EasyScraper.Parsing.ContentMiddleware.ContentMiddleware import ContentMiddleware
from EasyScraper.Parsing.ContentMiddleware.ContentMiddlewareBeautifulSoup import ContentMiddlewareBeautifulSoup
from EasyScraper.Parsing.PageParser.PageParser import PageParser
import urllib.parse


class PageParserPublication(PageParser):

    def getMiddlewares(self) -> [ContentMiddleware]:
        return [ContentMiddlewareBeautifulSoup()]

    def getURL(self) -> str:
        title_safe = urllib.parse.quote_plus(self.query)
        url = "https://scholar.google.de/scholar?q=" + title_safe
        return url

    def isContentAvailable(self) -> bool:
        return True

    def __getDivInfo(self):
        list_div_info = self.content.find_all("div", {"class": "gs_a gs_fma_p"})
        div_info = list_div_info[0]
        return div_info

    def parsePublicationDate(self) -> str:
        div_info_text = self.__getDivInfo().get_text()
        date = div_info_text.split("•")[0].strip()[-4:]
        return date

    def parsePublicationWebsite(self) -> str:
        div_info_text = self.__getDivInfo().get_text()
        publication_website = div_info_text.split("•")[1].strip()
        return publication_website

    def parsePublicationUrl(self) -> str:
        href_title = self.content.find_all(lambda tag: tag.name == "a" and self.query in tag.text)[0]
        publication_url = href_title['href']
        return publication_url
