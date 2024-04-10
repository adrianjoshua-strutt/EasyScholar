# This Scraper uses the Selenium

import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from EasyScholar.Scraper.WebScraper.WebScraper import WebScraper


class WebScraperSelenium(WebScraper):

    def getURLRAWContent(self, url) -> str:
        options = Options()
        options.add_argument("--headless")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Edge(options=options)
        driver.get(url)
        return driver.page_source
