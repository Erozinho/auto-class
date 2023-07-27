from flask import Flask, request
from bs4 import BeautifulSoup
import requests
import json



app = Flask(__name__)
app.config ['SECRET KEY'] = 'API123'



@app.route('/currency/<c1>/<c2>', methods=['GET', 'POST'])
def home(c1, c2):
    currency = get_currency(c1,c2)
    value = {'from':c1, 'to':c2, 'currency': currency}
    json_object = json.dumps(value, indent = 4) 
    return  json_object

def clean_text(currency, out):
    """Limpa o texto para informar o valor"""
    money = float(currency.split(" ")[0])
    return f"{money :.2f} {out}"


def get_currency(in_currency, out_currency):
    """Acessa o site de conversão e captura o valor exato"""
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    currency = soup.find('span', class_='ccOutputRslt').get_text()
    if len(currency) > 3:
        currency = currency.replace(",", "")
        return clean_text(currency, out_currency)
    return clean_text(currency, out_currency)


app.run()