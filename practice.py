import requests

api_key = '1b978f3c-43d5-4902-91b5-6c50133a3a4e'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()
for definitions in definitions:
    print(definitions)