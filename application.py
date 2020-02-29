import sys
import os
import shutil
from parse import Scraping

if __name__ == '__main__':
    arg = sys.argv[1]

    if arg == 'parse':
        obj = Scraping.Scraping()
        obj.parse()
        obj.db()
        
    elif arg == 'serve':
        shutil.copy('./db/movie.sqlite', './serve/')
        os.system('python serve/manage.py runserver 8080')