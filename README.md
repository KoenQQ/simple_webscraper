

# simple webscraper

You can use this simple tool to scrape webpages using the cli command 'python manage.py scrape'. Use this scraper to scrape webpages in a couple of minutes and see what they turn out. 

Adapt the scrape.py file to change what the scraper does exactly. 

The scraper runs on a django backend, you can use that as a base to expand it further. The big advantage in doing it this way is that you can automate the command using a scheduler (via Heroku for example). See the heading 'schedule the command' for more info on how to do this


# use
The scraper runs from the terminal and runs out of the box.


## activate env
the env makes sure the librariers of the scraper don't run afoul of the other libraries on your machine. 

cd to base folder
    
```
source env/bin/activate
```

## [first time use only] install libraries
you have to install all the libraries the first time you use it.


```
python -m pip install -r requirements.txt
```

## scrape command 


```
python manage.py scrape
```

arguments: 
- u [full url]

```
python manage.py scrape -u https://www.thedrive.com/
```

(you can also hardcode a standard url in scrape.py so you don't need to type in the url)

Scrape pulls in the page, parses it using beautifulsoup4 and spits it out in its base form in the terminal. Tune the scrape function to your liking to improve the outcome.


# further uses
The application runs on Django. You can use that to further expand on the scraper.

## schedule the command
You can push it to heroku and use the (free) heroku scheduler to make the command recurring. 

explainer: https://devcenter.heroku.com/articles/scheduling-custom-django-management-commands

## potential usecase
periodically scrape info from a website and store that in a database to compare prices. With the django backend you can easily add a postgres database to it and build an api that can get input from the database. 