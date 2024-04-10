from EasyScholar.Content.PublicationContent import PublicationContent
import csv

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

with open(file_publications, 'r', encoding='utf-8') as file:
    for publication_title in file:
        publication_title = publication_title.strip()
        publication_content = PublicationContent(publication_title)
        publication_contents.append(publication_content.toDict())
        print(publication_contents)

writeArrayOfDictsToCSVFile(publication_contents, file_output)
