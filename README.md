# Movie Review Data Scraping


## Installation Dependencies

### For Web scripting
```
$ pip install urllib beautifulsoup4 pysqlite3 
```

### For Web server
```
$ pip install django
```

## To run the programs

### To script data from Wiki
```
$ python application.py parse
```

### To run the server file
```
$ python application.py serve
```

### To sync with Database
```
$ python serve/manage.py migrate --run-syncdb
```