from bs4 import BeautifulSoup
import requests

in_currency = input('Enter the first Currency code:\n')
out_currency = input('Enter the second Currency code:\n')

def clean_text(currency, out):
    """Limpa o texto para informar o valor"""
    money = float(currency.split(" ")[0])
    return f"{money :.2f} {out}"
    

def get_currency(in_currency, out_currency):
    """Acessa o site e pega o valor da cotação"""
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    currency = soup.find('span', class_='ccOutputRslt').get_text()
    return clean_text(currency, out_currency)


print(get_currency(in_currency, out_currency))
