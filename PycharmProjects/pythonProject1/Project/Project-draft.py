import requests
import random


# You are given a card with random stats
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


def get_pokemon_card():
    pokemon_id = get_random_number()
    random_pokemon = get_pokemon(pokemon_id)
    return random_pokemon


pokemon_card = get_pokemon_card()

print("Your pokemon card is :")
print("Name " + str(pokemon_card["name"]))
print("Weight " + str(pokemon_card["weight"]))
print("Height " + str(pokemon_card["height"]))

# choose stat
player = int(input("Which stat would you like to play? Enter 1 for height and 2 for weight.\n"))
computer_card = get_pokemon_card()
player_stat = 0
computer_stat = 0

if player == 1:
    player_stat = pokemon_card["height"]
    computer_stat = computer_card["height"]
elif player == 2:
    player_stat = pokemon_card["weight"]
    computer_stat = computer_card["weight"]
else:
    print("Enter 1 for height or 2 for weight!")


# printing computers card
print("Computers pokemon card is :")
print("Name " + str(pokemon_card["name"]))
print("Weight " + str(pokemon_card["weight"]))
print("Height " + str(pokemon_card["height"]))

# comparisons for player vs computer
if computer_stat < player_stat:
    print("You win!")
elif computer_stat == player_stat:
    print("You Draw!")
else:
    print("You Lose!")
