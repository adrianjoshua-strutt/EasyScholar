# Will scrape until given ContentParser is available.
from EasyScraper.Scraping.ScrapingScheduler.ScrapingScheduler import ScrapingScheduler


class ScrapingSchedulerBruteforce(ScrapingScheduler):

    def scrape(self, parser):
        self.processParser(parser)
        while not parser.isContentAvailable():
            self.processParser(parser)
