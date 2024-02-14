from flask import Flask, render_template
from .model import PokeClient
app = Flask(__name__)
app.jinja_env.filters['zip'] = zip
poke_client = PokeClient()

@app.route('/')
def index():
    """
    Must show all of the pokemon names as clickable links

    Check the README for more detail.
    """
    pokemon_names = poke_client.get_pokemon_list()
    pokemon_ids = poke_client.get_pokemon_ids()
    return render_template('index.html', pokemon_names=pokemon_names, pokemon_ids=pokemon_ids, zip=zip)

@app.route('/pokemon/<pokemon_name>')
def pokemon_info(pokemon_name):
    """
    Must show all the info for a pokemon identified by name

    Check the README for more detail
    """
    pokemon_info = poke_client.get_pokemon_info(pokemon_name.lower())
    return render_template('pokemon_info.html', pokemon_info=pokemon_info)

@app.route('/ability/<ability_name>')
def pokemon_with_ability(ability_name):
    list_of_pokemons_with_ability = poke_client.get_pokemon_with_ability(ability_name.lower())
    # We need the list of pokemon ids only for the list of pokemons with the ability
    return render_template('pokemon_with_ability.html', ability_name=ability_name, list_of_pokemons_with_ability=list_of_pokemons_with_ability)