

# EasyScholar - A Google Scholar Scraper

`EasyScholar` is a simple library to scrape Google Scholar using publication titles.

**NOTE: This library is only for small scraping (e.g. 20 papers)**

Building on EasySchoolar I created `PublicationsToCSV`.
Given a list of publication titles it turns them into a CSV file containg more information (via BeautifulSoup).

This tool was created while writing my master thesis. I had several related work papers I needed to compare. I only had a list of publications, but needed a a .csv file enriched with information (e.g. publication date).

## Usage

### Scrape data from single publication via title 

    from EasyScholar.PublicationContent import PublicationContent  
      
    content = PublicationContent('Discriminative unsupervised feature learning with convolutional neural networks')  
      
    print(content.getDate()) # Output: 2014  
    print(content.getPublicationWebsite()) # Output: proceedings.neurips.cc  
    print(content.getPublicationUrl()) # Output: https://proceedings.neurips.cc/paper/2014/hash/07563a3fe3bbe7e3ba84431ad9d055af-Abstract.html

