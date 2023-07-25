from bs4 import BeautifulSoup
import requests

print("Any of manys currency code: AUSTRALIA:AUD, UE:EUR, USA:USD, BRAZIL:BRL, MEXICO:MXN, JAPAN:JPY")
in_currency = input('Enter your currency code:\n')
out_currency = input('Enter the desired currency code:\n')
amount = input('Amount of money:\n')


def clean_text(currency, out):
    """Limpa o texto para informar o valor"""
    money = float(currency.split(" ")[0])
    return f"{money :.2f} {out}"


def get_currency(in_currency, out_currency, amount):
    """Acessa o site de conversão e captura o valor exato"""
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={amount}"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    currency = soup.find('span', class_='ccOutputRslt').get_text()
    if len(currency) > 3:
        currency = currency.replace(",", "")
        return clean_text(currency, out_currency)
    return clean_text(currency, out_currency)


print(get_currency(in_currency, out_currency, amount))
