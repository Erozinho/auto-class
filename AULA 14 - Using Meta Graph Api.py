import requests
import json

token = input('API token: ')
url = f"https://graph.facebook.com/v17.0/4106083466172974?fields=link%2Cimages&access_token={token}"

response = requests.get(url)

data = response.text

data = json.loads(data)
image_url = (data['images'][0]['source'])

image_bytes = requests.get(image_url).content

with open('automations-lessons/image.jpg', 'wb') as file:
    file.write(image_bytes)
