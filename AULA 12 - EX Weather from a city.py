import requests

def get_weather():
    """Pega o json da API e organiza de acordo"""
    url = f'https://api.openweathermap.org/data/2.5/forecast?lat=-23.53&lon=-46.78&appid=5a56265795331715b0814ea8eb5d1a3b&units=metric'

    result = requests.get(url)
    r = result.json()

    # Pega o nome da cidade
    city = r['city']['name']

    # Abre o arquivo desejado
    with open('automations-lessons\AULA12.txt', 'a', encoding='utf-8') as file:

        # Percorre a lista de informações recolhendo os valores desejados
        for x in r['list']:

            # Busca a temperatura
            temp= x['main']['temp']

            # Busca o dia do ano + as horas
            dt = x['dt_txt']

            # Condição do tempo naquele dia/hora
            condition = x['weather'][0]['description']

            # Concatena tudo junto
            txt = f"{city},{dt},{temp},{condition}"

            file.write(f'{txt}\n')


print(get_weather())
