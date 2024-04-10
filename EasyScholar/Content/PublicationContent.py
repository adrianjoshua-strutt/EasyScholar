from EasyScholar.Scraper.ScholarScraper import ScholarScraper
from EasyScholar.Scraper.WebScraper.WebScraperRequests import WebScraperRequests


class PublicationContent:

    def __init__(self, title, scholar_scraper=None):
        if scholar_scraper is None:
            self.scholar_scraper = ScholarScraper(WebScraperRequests())
        if type(title) is str:
            self.content = self.scholar_scraper.getPublicationContent(title)
            self.title = title
        else:
            raise TypeError("PublicationContent should be provided with string, " + str(title) + "provided")

    def __getDivInfo(self):
        list_div_info = self.content.find_all("div", {"class": "gs_a gs_fma_p"})
        div_info = list_div_info[0]
        return div_info

    def getDate(self) -> str:
        div_info_text = self.__getDivInfo().get_text()
        date = div_info_text.split("•")[0].strip()[-4:]
        return date

    def getPublicationWebsite(self) -> str:
        div_info_text = self.__getDivInfo().get_text()
        publication_website = div_info_text.split("•")[1].strip()
        return publication_website

    def getPublicationUrl(self) -> str:
        href_title = self.content.find_all(lambda tag: tag.name == "a" and self.title in tag.text)[0]
        publication_url = href_title['href']
        return publication_url

    def toDict(self) -> dict:
        return {
            "date": self.getDate(),
            "publication_website": self.getPublicationWebsite(),
            "publication_url": self.getPublicationUrl(),
        }

    def __str__(self) -> str:
        return self.toDict().__str__()
