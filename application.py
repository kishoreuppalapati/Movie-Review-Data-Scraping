import sys
from parse import Scraping

if __name__ == '__main__':
    arg = sys.argv[1]

    if arg == 'parse':
        obj = Scraping.Scraping()
        obj.parse()
        obj.db()
    else:
        print('Working!!!!!!!')