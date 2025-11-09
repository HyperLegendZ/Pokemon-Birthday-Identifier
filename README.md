# ⚡ Pokemon Birthday Identifier 🎂

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)

**Gotta Match 'Em All!** Have you ever wondered which Pokémon you share a birthday with? This Python tool is your Pokédex for identifying your perfect Pocket Monster companion based on the month and day you entered the world!

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

```bash
python pokemon_birthday.py
