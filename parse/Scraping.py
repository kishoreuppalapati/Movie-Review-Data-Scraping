from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re
import sqlite3


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
            
        #print(self.name, self.year)
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
        
    def db(self):
        con = sqlite3.connect('./serve/db/movie.sqlite')
        cur = con.cursor()

        cur.execute('DROP TABLE IF EXISTS Movie')
        cur.execute('CREATE TABLE Movie(ID INT PRIMARY KEY NOT NULL, Name TEXT NOT NULL, YearNo INT NOT NULL, Awards VARCHAR(25) NOT NULL)')

        for i in range(len(self.name)):
            id = i + 1
            n = self.name[i]
            y = int(self.year[i])
            a = (self.awards[i])

            cur.execute('SELECT ID FROM Movie WHERE Name = ?', (n,))
            row = cur.fetchone()

            if row is None:
                cur.execute('INSERT INTO Movie(ID, Name, YearNo, Awards) VALUES(?, ?, ?, ?)', (id, n, y, a))
                print("%d%% Data is instered into Database" % int(i / len(self.name) * 100))
            
            con.commit()

        cur.close()