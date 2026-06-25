import requests

response = requests.get('https://dummyjson.com/products')
data = response.json()
print(data)