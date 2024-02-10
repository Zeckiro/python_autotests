"""
Pokemon test
"""
import requests

URL = 'https://api.pokemonbattle.me/v2'
HEADER = {'Content-Type': 'application/json', 'trainer_token': 'dccb884649b8f84f932357f8fc563187'}

body = {
    "name": "MainLOL",
    "photo": "https://dolnikov.ru/pokemons/albums/065.png"
}
response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(response.text)

URL = 'https://api.pokemonbattle.me/v2'
HEADER = {'Content-Type': 'application/json', 'trainer_token': 'dccb884649b8f84f932357f8fc563187'}

body = {
    "pokemon_id": "30000"
}
response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
print(response.text)

URL = 'https://api.pokemonbattle.me/v2'
HEADER = {'Content-Type': 'application/json', 'trainer_token': 'dccb884649b8f84f932357f8fc563187'}

body = {
    "pokemon_id": "30000",
    "name": "Zawarka",
    "photo": "https://dolnikov.ru/pokemons/albums/065.png"
}
response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(response.text)