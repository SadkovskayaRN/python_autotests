import requests

URL = 'https://api.pokemonbattle.me/v2'
token = '25ce57e72e8d1c91bedf91fa5737919f'
header = {'Content-Type': 'application/json', 'trainer_token': token}



# Создание покемона

body_create = {
    "name": "Плюша",
    "photo": "https://dolnikov.ru/pokemons/albums/002.png"
}

response_create = requests.post(url=f'{URL}/pokemons', headers=header, json=body_create)
print(response_create.text)

# Вывести список моих покемонов активных

params = {
    "trainer_id": 2791,
    "status": 1,
    "in_pokeball" : 0
}

response_spisok = requests.get(url=f'{URL}/pokemons', headers=header, params=params)
pokemon_list = response_spisok.json()

print(pokemon_list)

if 'data' in pokemon_list and pokemon_list['data']:
    first_pokemon_id = pokemon_list['data'][0]['id']
    print(first_pokemon_id)
    
    # Определение переменной pokemon_id
    pokemon_id = first_pokemon_id

else:
    print("Список покемонов пуст")


# Изменение покемона
body_update_pokemon = {
    "pokemon_id": pokemon_id,
    "name": "Пушинка",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

'''response_update_pokemon = requests.put(url=f'{URL}/pokemons', headers=header, json=body_update_pokemon)
print(response_update_pokemon.json())'''

# Поймать в покебол

body_poymat_pokebol = {
    "pokemon_id": pokemon_id
}

response_poymat_pokebol = requests.post(url=f'{URL}/trainers/add_pokeball', headers=header, json=body_poymat_pokebol)
print(response_poymat_pokebol.text)






