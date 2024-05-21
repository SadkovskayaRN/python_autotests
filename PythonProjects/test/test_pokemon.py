import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
token = '25ce57e72e8d1c91bedf91fa5737919f'
header = {'Content-Type': 'application/json', 'trainer_token': token}

def test_sttus_code ():
    
    response_spisok_trenerov = requests.get(url=f'{URL}/trainers', headers=header)
    assert response_spisok_trenerov.status_code == 200

def test_name ():
    trainer_id = 2791
    
    response_spisok_trenerov = requests.get(url=f'{URL}/trainers', headers=header, params={'trainer_id': trainer_id})
    assert response_spisok_trenerov.json()["data"][0]["trainer_name"] == 'Звездочка'




    

    







