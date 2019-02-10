import json
import os
import requests

def main():
    # url = "https://www.goodreads.com/search.xml?key={}&q=Ender%27s+Game".format(os.getenv('GOODREADS_KEY'))
    url = "https://www.goodreads.com/owned_books/{}?format=xml".format(os.getenv('USER_ID'))
    print (url)

    params = {
        'key': os.getenv('GOODREADS_KEY'),
        'format': 'xml',
        'id': os.getenv('USER_ID'),
    }
    print (params)
    r = requests.get(url) #, params=params)
    return r.text


if __name__ == "__main__":
    print (main())
