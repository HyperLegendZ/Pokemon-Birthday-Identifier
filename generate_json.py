import json
import requests

OUTPUT_FILE = "pokemon_birthdays.json"

# ✅ Get ALL Pokémon in ONE request
url = "https://pokeapi.co/api/v2/pokemon?limit=1025"
response = requests.get(url)

if response.status_code != 200:
    print("❌ Failed to fetch Pokémon data")
    input("Press Enter to exit...")
    exit()

data = response.json()

# Extract names
pokemon_list = [p["name"] for p in data["results"]]

# ✅ Generate valid calendar days
days = []
for m in range(1, 13):
    for d in range(1, 32):
        if (m == 2 and d > 28) or (m in [4, 6, 9, 11] and d > 30):
            continue
        days.append(f"{d:02}{m:02}")

# ✅ Map each day → ONE Pokémon
result = {}
for i, day in enumerate(days):
    result[day] = pokemon_list[i % len(pokemon_list)]

# Save JSON
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)

print("✅ pokemon_birthdays.json created successfully!")
input("Press Enter to exit...")
