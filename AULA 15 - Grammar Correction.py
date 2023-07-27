import requests
import json

url = "https://api.languagetoolplus.com/v2/check"
data = {'text': 'Vose estar muinto erredo!', 'language': 'pt-br'}

response = requests.post(url, data=data, verify=False)
response = json.loads(response.text)
print(response['software'])