# Given a list of Parser Objects this list scrapes all of them in a naive way, without checking for availability
from EasyScraper.Scraping.ScrapingScheduler.ScrapingScheduler import ScrapingScheduler


class ScrapingSchedulerNoCheck(ScrapingScheduler):

    def scrape(self, parser):
        self.processParser(parser)
