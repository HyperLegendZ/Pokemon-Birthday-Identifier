import json
import os

FILE_NAME = "pokemon_birthdays.json"

# Get the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, FILE_NAME)

# Load JSON safely
try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Error: {FILE_NAME} not found in the script folder.")
    input("Press Enter to exit...")
    exit()
except json.JSONDecodeError:
    print("Error: JSON file is corrupted or not valid JSON.")
    input("Press Enter to exit...")
    exit()

# Get user input
bday = input("Enter birthday (DDMM): ")

# Validate input
if not bday.isdigit() or len(bday) != 4:
    print("❌ Invalid format. Use DDMM (e.g. 0705)")
    input("Press Enter to exit...")
    exit()

# Look up Pokémon
pokemon = data.get(bday)

if pokemon:
    print(f"\n🔥 Your Pokémon is: {pokemon.title()}")
else:
    print("\n❌ No Pokémon found for that date")

input("\nPress Enter to exit...")