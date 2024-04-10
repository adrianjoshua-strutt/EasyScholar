from EasyScholar.Content.PublicationContent import PublicationContent
import csv

from EasyScholar.Scraper.ScholarScraper import ScholarScraper
from EasyScholar.Scraper.WebScraper.WebScraperRequests import WebScraperRequests

file_publications = "C:\\Users\\Joshua\\Desktop\\publications.txt"
file_output = "C:\\Users\\Joshua\\Desktop\\publications.csv"


def writeArrayOfDictsToCSVFile(dicts, filename):
    fieldnames = list(dicts[0].keys())
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in dicts:
            writer.writerow(row)


publication_contents = []

scraper = ScholarScraper(WebScraperRequests())

with open(file_publications, 'r', encoding='utf-8') as file:
    for publication_title in file:
        publication_title = publication_title.strip()
        publication_content = PublicationContent(publication_title, scraper)
        publication_contents.append(publication_content.toDict())

writeArrayOfDictsToCSVFile(publication_contents, file_output)
