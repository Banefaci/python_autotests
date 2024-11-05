import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '64e12e7140a68fea6d1133eadbb49929'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

body_change = {
    "pokemon_id": "124027",
    "name": "Lolp",
    "photo_id": -1
}

body_catch = {
    "pokemon_id": "124031"
}

responce_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(responce_create.text)

responce_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(responce_change.text)

responce_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(responce_catch .text) 