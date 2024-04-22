import requests

api_key = 'c7f8aa82-3037-4818-8f8e-1b9f68d039fd'
word = 'cloud'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(final_url)
result = r.json()
print(result)
