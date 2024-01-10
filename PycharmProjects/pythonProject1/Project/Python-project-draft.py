# Play multiple rounds

import requests
import random


def get_random_number():
    return random.randint(1, 151)


def get_pokemon(id):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(id)
    response = requests.get(url).json()
    pokemon = {
        "id": id,
        "name": response["name"],
        "height": response["height"],
        "weight": response["weight"]
    }
    return pokemon


def chose_pokemon():
    my_pokemon_amount = int(input("how many pokemon do you want to chose from? "))

    my_pokemons = []
    my_pokemon_ids = []

    for i in range(my_pokemon_amount):
        pokemonid = get_random_number()

        while (pokemonid in my_pokemon_ids):
            pokemonid = get_random_number()

        my_pokemon_ids.append(pokemonid)
        my_pokemons.append(get_pokemon(pokemonid))

    print("These are your pokemons: \n")

    counter = 0
    for pokemon in my_pokemons:
        print("Number: " + str(counter))
        print("Name: " + pokemon["name"])
        print("Height: " + str(pokemon["height"]))
        print("weight: " + str(pokemon["weight"]))
        print("\n")
        counter += 1
    return my_pokemons[int(input("Enter the number of the pokemon you chose. "))]


def play_round(my_pokemon, computer_pokemon, my_score, computer_score):
    stat = input("Which stat do you want to use? (weight or height) ")
    if (my_pokemon[stat] > computer_pokemon[stat]):
        print("you won")
        my_score = my_score + 1
    elif (my_pokemon[stat] < computer_pokemon[stat]):
        print("computer won")
        computer_score = computer_score + 1
    else:
        print("it's a draw")
    return my_score, computer_score


# Start of program
round_amount = int(input("how many rounds do you want to play? "))

my_score = 0
computer_score = 0

for i in range(round_amount):
    print("Round ", i + 1)
    my_pokemon = chose_pokemon()
    print("You chose " + my_pokemon["name"])

    computer_pokemon_id = get_random_number()
    computer_pokemon = get_pokemon(computer_pokemon_id)
    print("Computer chose " + computer_pokemon["name"])
    my_score, computer_score = play_round(my_pokemon, computer_pokemon, my_score, computer_score)

if (my_score > computer_score):
    print("you won!")
elif (my_score < computer_score):
    print("computer won :(")
else:
    print("It's a draw")

print("your total score is ", my_score)
print("computer total score is ", computer_score)

