from app import app
import requests

from flask import render_template

@app.route('/')
def land():
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

    poke_dict1 = func('gyarados')

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

    poke_dict2 = func('zapdos')

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

    poke_dict3 = func('mewtwo')

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

    poke_dict4 = func('ditto')

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

    poke_dict5 = func('mew')
    return render_template('index.html', mew = poke_dict5, ditto = poke_dict4, mewtwo = poke_dict3, zapdos = poke_dict2, gyarados = poke_dict1)

@app.route('/home')
def home():
    return 

@app.route('/register')
def test():
    return 

