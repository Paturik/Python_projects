import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape (self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        with open ("news.txt", "w") as f:
            for tag in sp.find_all("a"):
                url = tag.get ("href")
                if url is None:
                    continue
                if "html" and url in url:
                    print ("\n" + url)
                    f.write(url + "\n")

   
        

news = "https://www.ukr.net/"
Scraper (news).scrape()
