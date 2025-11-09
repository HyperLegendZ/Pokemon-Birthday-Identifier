# ⚡ Pokemon Birthday Identifier 🎂


**Gotta Match 'Em All!** Have you ever wondered which Pokémon you share a birthday with? This Python tool is your Pokédex for identifying your perfect companion based on the month and day you entered the world!

---

## ✨ Features

* **Date-to-Dex Match:** Quickly matches your birth month and day (in `DDMM` format) to a specific Pokémon's identifier in a custom database.
* **Simple Interface:** Get your result with a single command line prompt. No need for a Master Ball to figure this out!
* **Expandable Data:** Easily grow the Pokédex by adding more Pokémon and corresponding birthday numbers to the `pokemon_index.json` file.

---

## 🚀 Get Started

### Prerequisites

You only need **Python 3** installed to run this script.

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone [Your Repository URL Here]
    cd Pokemon-Birthday-Identifier
    ```
2.  **Verify Data:** Ensure your `pokemon_index.json` file is correctly formatted and contains the `"bday"` field for each Pokémon.

### How to Run

Execute the script from your terminal:

1. **Get the right directory.     *This tends to be the accounts' username.***
   ```bash
   cd "C:\Users\____*\Documents\Project Pokemon Bday"
   ```
2. **Paste this into the terminal to start the code.**
    ```bash
    python "pokemon birthday.py"
    ```

### Example Session

```bash
python pokemon_birthday.py
Enter the your birthday (DDMM): 0728
```

✅ Found a Pokémon with the pokemon index number 0728:
- Popplio

---

## 📂 Project Structure

This is how the file is formatted.

| File | Description |
| :--- | :--- |
| `pokemon_birthday.py` | The main Python script handling user input, JSON loading, and search logic. |
| `pokemon_index.json` | The core database file containing Pokémon names and their associated `"bday"` value (the birthday number used for matching). |
| `README.md` | The project overview file you're reading! |

## 📝 Notes

Pokemon index was mainly taken from Pokemon showdown and edited.
Link: https://play.pokemonshowdown.com/data/pokedex-mini-bw.js
Small Project may be improved on!

