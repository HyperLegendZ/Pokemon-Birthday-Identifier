import json

# Constants
FILE_NAME = "pokemon_index.json"

# --- 1. Get user input for 'bday' condition ---
bday_input = input("Enter the Pokémon's birthday (DDMM): ")

# --- 2. Load the JSON file ---
try:
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        pokemon_data = json.load(f)
except FileNotFoundError:
    print(f"Error: The file '{FILE_NAME}' was not found.")
    exit()
except json.JSONDecodeError as e:
    print(f"Error decoding JSON file: {e}")
    # This error usually means a missing comma or quote in the JSON.
    exit()

# --- 3. Search for Pokémon matching the 'bday' condition ---
found_pokemon = []
for name, info in pokemon_data.items():
    # The 'bday' value in your JSON (like 38 or 39) appears to be an integer.
    # We must convert the string input to an integer to match the JSON data type.
    try:
        bday_condition = int(bday_input)
    except ValueError:
        print("\nInvalid input. Please enter a number (DDMM).")
        exit()

    # The search condition: Check if the Pokémon's 'bday' value matches the user's input
    if info.get("bday") == bday_condition:
        found_pokemon.append(name.title()) # .title() makes names like 'jigglypuff' look nice

# --- 4. Display results ---
if found_pokemon:
    print(f"\n✅ Found a Pokémon with birthday number {bday_input}:")
    for name in found_pokemon:
        print(f"- {name}")
else:
    print(f"\nNo Pokémon found with birthday number {bday_input}.")
