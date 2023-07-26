import requests

def get_news(country, api_key='057a19ba5af941e2addba5265f0b265e'):
    """Seta as preferencias na URL e aleatoriaza um topico"""
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    article = content['articles']
    results = []
    for article in article:
        results.append(F"TITLE\n{article['title']}, \nDESCRIPTION: {article['description']}")
    return results


country = input('Enter your desire Country(us, br, fr, jp...):\n')

print(get_news(country))
