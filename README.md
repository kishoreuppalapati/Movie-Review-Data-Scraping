# Movie Review Data Scraping

In this assignment, you need to read data from multiple sources, structure them, and make them available by providing a simple REST API. Once you complete the assignment you’ll have a simple  RESTful  interface  using  which  users  can  interact  and  find  information  about  different movies.  Your  application  should  support  HTTP  clients.  People  should  be  able  to  use CURL, Postmanor any other REST client to interact with your web service.

## Installation Dependencies

* (Install Python Version - 3.6)[https://www.python.org/downloads/release/python-3610/]
```
$ pip install urllib beautifulsoup4 pysqlite3 

$ pip install django

$ pip install djangorestframework
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


### API Endpoints
```
http://localhost:8080/movie/
http://localhost:8080/movie/3 (Id number 3)
http://localhost:8080/movie/name (Provide the movie name with Id)
http://localhost:8080/movie/year (Provide the movie list with year)
http://localhost:8080/movie/year/2017 (Provide the movie name according to year)
```