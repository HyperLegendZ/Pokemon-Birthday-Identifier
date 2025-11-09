import json

Bday = input("Enter your Pokémon's birthday (MMDD): ")

with open("pokemon_index.json", "r") as f:
    pokemon_data = json.load(f) 

print (pokemon_data.get(Bday, "No Pokémon with that birthday found."))
#Bday = input("Enter your Pokémon's birthday (MMDD): ")
#if Bday in pokemon_data:
    #print(pokemon_data[Bday])
#else:
    #print("No Pokémon with that birthday found.")
