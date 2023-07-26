import requests
from random import randint as rn

# content = r.json()
# articles = content['articles']
# print(type(articles))

# for x in articles:
    # print('TITLE:\n',x['title'],
          # '\nDESCRIPTION:\n',x['description'])

def get_news(topic, from_date, to_date, api_key='057a19ba5af941e2addba5265f0b265e'):
    """Seta as preferencias na URL e aleatoriaza um topico"""
    url = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language=en&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    total = content['totalResults']
    articles = content['articles']
    rint = rn(0,total-1)
    title = f"TITLE:\n{articles[rint]['title']}\n"
    desc = f"DESCRIPTION:\n{articles[rint]['description']}"
    return title + desc


topic = input('Enter your desire topic:\n')
from_date = input('Enter the starter date in this format(yyyy-mm-dd):\n')
to_date = input('Enter the end date in this format(yyyy-mm-dd):\n')

if " " in topic:
    topic.replace(" ", "%20")

print(get_news(topic, from_date, to_date))
