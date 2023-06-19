import requests

def func(poke):
    data_dict = {}
    res1 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}')
    data = res1.json()
    data_dict['name'] = data['name']
    data_dict['abilities'] = data['abilities'][0]['ability']
    data_dict['base_experience'] = data['base_experience']
    data_dict['attack'] = data['stats'][0]
    data_dict['attack'] = data['stats'][1]
    data_dict['defense'] = data['stats'][2]
    data_dict['special-attack'] = data['stats'][3]
    data_dict['sprites'] = data['sprites']['front_shiny']
    return data_dict
poke = func('gyarados')
print(poke['sprites'])