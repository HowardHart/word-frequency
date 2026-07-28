# word_frequency_counter
A simple Python script to count word frequencies in a text file.

## Features
- Read `.txt` file
- Clean text (lowercase, remove punctuation)
- Tokenize and count word frequencies
- Display top N frequent words
- Calculate token count (total words)
- Calculate type count (unique words)
- Calculate type/token ratio (TTR)
- Export results to CSV

## Repository Structure
- `word_frequency.py` – Python script version (run directly)
- `word_frequency.ipynb` – Jupyter Notebook version (step-by-step analysis)
- `sample.txt` – Example text file for testing
- `requirements.txt` – List of Python dependencies
- `README.md` – Project documentation (this file)

## Requirements
- Python 3.x
- pandas

## Usage
1. Place your text file as `sample.txt` in the same folder (or modify the `input_file` variable in the script)
2. Run the script:
   ```bash
   python word_frequency.py
