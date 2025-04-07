import requests

url = 'https://api.chucknorris.io/jokes/random'
response = requests.get(url)

if response.status_code == 200:
    print("Success!")
    data = response.json()
    
    print("Essa eh a piada do Chuck Norris:")
    print(data['value'])
else:
    print("Error:", response.status_code)
