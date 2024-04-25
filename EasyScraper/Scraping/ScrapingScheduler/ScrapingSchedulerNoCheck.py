# Given a list of Parser Objects this list scrapes all of them in a naive way, without checking for availability
from EasyScraper.Scraping.ScrapingScheduler.ScrapingScheduler import ScrapingScheduler


class ScrapingSchedulerStandard(ScrapingScheduler):

    def scrape(self):
        for parser in self.parserList:
            self.processParser(parser)
            print(parser.parsePublicationUrl())
            print(parser)
