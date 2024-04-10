import bs4
import requests
from bs4 import BeautifulSoup
import urllib.parse


def getURLFromTitle(title) -> str:
    title_safe = urllib.parse.quote_plus(title)
    url = "https://scholar.google.de/scholar?q=" + title_safe
    return url


def getURLContent(url) -> bs4.BeautifulSoup:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def getPublicationContent(title) -> bs4.BeautifulSoup:
    url = getURLFromTitle(title)
    content = getURLContent(url)
    return content
