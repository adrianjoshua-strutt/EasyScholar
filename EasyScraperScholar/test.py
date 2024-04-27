from EasyScraper.Scraping.PageScraper.PageScraperRequests import PageScraperRequests
from EasyScraper.Scraping.PageScraper.PageScraperSelenium import PageScraperSelenium
from EasyScraper.Scraping.ScrapingScheduler.ScrapingSchedulerNoCheck import ScrapingSchedulerNoCheck
from EasyScraperScholar.ContentParserPublication import ContentParserPublication

scraper = ScrapingSchedulerNoCheck(PageScraperSelenium())
parser = ContentParserPublication("{SCRAPS}: Scalable Collective Remote Attestation for {Pub-Sub}{IoT} Networks with Untrusted Proxy Verifier")
scraper.scrape(parser)
print(parser)