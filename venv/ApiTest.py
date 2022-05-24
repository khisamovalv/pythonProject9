import requests


def get_weather_by_city(city_name):
    url = 'https://goweather.herokuapp.com/weather/moscow'
    weather = requests.get(url).json()
    return weather

#print(weather.keys())
#print(weather['temperature'])
#print(get_weather_by_city('Kazan'))

def print_fun_facts():
    url = 'https://cat-fact.herokuapp.com/facts'
    for i in range (4):
        print(requests.get(url).json()[i]['text'])

#print_fun_facts()
#def get_authors_books():
    #url = 'https://openlibrary.org/works/OL45883W.json'
    #for i in range():
    #for i in range(10):
    #print(requests.get(url).json().keys())
    #response = requests.get(url).json()['authors']
    #print(response[0]['author']['key'])
    #print(author['key': '/authors/OL34184A'])
#get_authors_books()

url = 'https://openlibrary.org/authors/OL23919A/works.json'
print(requests.get(url).json().keys())