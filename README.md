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

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/HyperLegendZ/Pokemon-Birthday-Identifier
    cd Pokemon-Birthday-Identifier
    ```
2.  **Verify Data:**
       Ensure your `pokemon_index.json` file is correctly formatted and contains the `"bday"` field for each Pokémon.
3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

### ▶️ How to use
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




This project uses:

requests

