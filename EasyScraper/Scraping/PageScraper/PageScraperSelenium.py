# This Scraper uses the Selenium
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from EasyScraper.Scraping.PageScraper.PageScraper import PageScraper


class PageScraperSelenium(PageScraper):

    def getContent(self, url) -> str:
        options = Options()
        options.add_argument("--headless")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Edge(options=options)
        driver.get(url)
        return driver.page_source
