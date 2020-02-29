from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re


class Scraping:
    def __init__(self):
        self.url = 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'
        self.name = []
        self.year = []
        self.link = []
        self.awards = []
        self.nomination = []
    
    def parse(self):
        page = urlopen(self.url)
        html = page.read()
        html_out = soup(html, 'lxml')
        #print(html_out.prettify())


        right_table = html_out.find('table', class_='wikitable sortable')

        for row in right_table.findAll('tr'):
            cells = row.findAll('td')
            if len(cells) == 4:
                self.name.append(cells[0].find(text=True))
                
                li = cells[0].findAll('a')
                match = re.search(r'href=[\'"]?([^\'" >]+)', str(li))
                if match:
                    temp = match.group(0)
                    self.link.append('https://en.wikipedia.org'+temp[6:])

                self.year.append(cells[1].find(text=True))
                self.awards.append(cells[2].find(text=True))
                self.nomination.append(cells[3].find(text=True))
            
        print(self.name, self.year)
        page.close()

    def parseMovieSite(self):
        for newpage in self.link:
            page = urlopen(newpage)
            html = page.read()
            html_out = soup(html, 'lxml')

            r = html_out.find('table', class_='infobox vevent')
            if r != None:
                for row in r.findAll('tr'):
                    head = row.th
                    value = row.td

                    if head and value:    
                        head = str(head.contents)
                        value = str(value.contents)
                        print(head, value)
            
            page.close()
        