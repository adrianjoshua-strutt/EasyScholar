import csv
from EasyScraper.Scraping.ScrapingScheduler.ScrapingSchedulerNoCheck import ScrapingSchedulerStandard
from EasyScraperScholar.PageParserPublication import PageParserPublication

file_publications = "C:\\Users\\Joshua\\Desktop\\publications.txt"
file_output = "C:\\Users\\Joshua\\Desktop\\publications.csv"


def writeArrayOfDictsToCSVFile(dicts, filename):
    fieldnames = list(dicts[0].keys())
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in dicts:
            writer.writerow(row)


parser_list = []

with open(file_publications, 'r', encoding='utf-8') as file:
    for publication_title in file:
        publication_title = publication_title.strip()
        publication_parser = PageParserPublication(publication_title)
        parser_list.append(publication_parser)

page_parser = ScrapingSchedulerStandard(parser_list)

page_parser.scrape()

dict_list = []

for scraper in parser_list:
    dict_list.append(scraper.toDict())

writeArrayOfDictsToCSVFile(dict_list, file_output)
