import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '64e12e7140a68fea6d1133eadbb49929'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '6848'

def test_status_code ():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_resp ():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Дядя Ешта'