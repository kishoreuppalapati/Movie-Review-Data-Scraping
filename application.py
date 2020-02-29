import sys
import os
from parse import Scraping
#from serve import MovieApi

if __name__ == '__main__':
    arg = sys.argv[1]

    if arg == 'parse':
        obj = Scraping.Scraping()
        obj.parse()
        obj.db()
        
    elif arg == 'serve':
        os.system('python serve/manage.py runserver')