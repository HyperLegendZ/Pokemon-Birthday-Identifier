# ⚡ Pokemon Birthday Identifier 🎂


**Gotta Match 'Em All!** Have you ever wondered which Pokémon you share a birthday with? This Python tool is your Pokédex for identifying your perfect companion based on the month and day you entered the world!

---

## ✨ Features

* **Date-to-Dex Match:** Quickly matches your birth month and day (in `DDMM` format) to a specific Pokémon's identifier in a custom database.
* **Simple Interface:** Get your result with a single command line prompt. No need for a Master Ball to figure this out!
* **Expandable Data:** Easily grow the Pokédex by adding more Pokémon and corresponding birthday numbers to the `pokemon_index.json` file (if you want to of course).

---

## 🚀 Get Started

### Prerequisites

You only need **Python 3** installed to run this script.

### Installation

**Clone the Repository(in the terminal):**
```bash
git clone https://github.com/HyperLegendZ/Pokemon-Birthday-Identifier
```
**Open the file in the terminal**
```bash
cd Pokemon-Birthday-Identifier
```
**Install Dependencies**
```bash
pip install -r requirements.txt
```

### ▶️ How to use

Make sure you are putting all these commands into the file opened terminal! It should look something like:
"C:\Users\______\Pokemon-Birthday-Identifier>"

**Step 1: Generate the dataset**
```bash
python generate.py
```

This creates/updates pokemon_birthdays.json.

**Step 2: Run the app**
```bash
python main.py
```

Then enter your birthday in DDMM format:

Enter birthday (DDMM): 0705
🔥 Your Pokémon is: Pikachu




**This project uses:**
requests
