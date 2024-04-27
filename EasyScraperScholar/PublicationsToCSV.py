import csv

from EasyScraper.Scraping.PageScraper.PageScraperRequests import PageScraperRequests
from EasyScraper.Scraping.ScrapingScheduler.ScrapingSchedulerBruteforce import ScrapingSchedulerBruteforce
from EasyScraper.Scraping.ScrapingScheduler.ScrapingSchedulerNoCheck import ScrapingSchedulerNoCheck
from EasyScraperScholar.ContentParserPublication import ContentParserPublication

file_publications = "C:\\Users\\Joshua\\Desktop\\publications.txt"
file_output = "C:\\Users\\Joshua\\Desktop\\publications.csv"


def writeListOfDictsToCSVFile(dicts, filename):
    fieldnames = list(dicts[0].keys())
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in dicts:
            writer.writerow(row)


def getPublicationTitles():
    publication_titles = []
    with open(file_publications, 'r', encoding='utf-8') as file:
        for title in file:
            title = title.strip()
            publication_titles.append(title)
    return publication_titles


def parsersToDictList(list_parsers):
    dict_list = []
    for parser in parsers:
        dict_list.append(parser.toDict())
    return dict_list


scraper = ScrapingSchedulerBruteforce(PageScraperRequests())
parsers = [ContentParserPublication(title) for title in getPublicationTitles()]
[scraper.scrape(parser) for parser in parsers]
writeListOfDictsToCSVFile(parsersToDictList(parsers), file_output)
