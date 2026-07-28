# -*- coding: utf-8 -*-
"""
Word Frequency Counter

A simple Python script to count word frequencies in a text file.

Features:
- Read text file (.txt)
- Clean text (lowercase, remove punctuation)
- Tokenize and count word frequencies
- Display top N frequent words
- Calculate token count (total words)
- Calculate type count (unique words)
- Calculate type/token ratio (TTR)
- Export results to CSV
Usage:
    python word_frequency.py

Requires:
    Python 3.x
    pandas

Input:  .txt file (default: sample.txt)
Output: .csv file (default: word_frequency.csv)

Author: HowardHart
"""

import re
import pandas as pd
from collections import Counter

# ==================== 1. Read text file ====================
def read_text(file_path):
    """
    Read the content of a text file and return as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        print(f"[SUCCESS] Successfully read file: {file_path}")
        return text
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return None

# ==================== 2. Clean text ====================
def clean_text(text):
    """
    Clean the text: convert to lowercase, remove punctuation.
    Keeps only letters, digits, and whitespace.
    """
    text = text.lower()
    # Keep only alphanumeric characters and spaces
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

# ==================== 3. Tokenize ====================
def tokenize(text):
    """
    Split cleaned text into a list of words.
    """
    words = text.split()
    # Filter out empty strings
    words = [w for w in words if w]
    return words

# ==================== 4. Count word frequency ====================
def count_word_frequency(words):
    """
    Count frequency of each word using Counter.
    Returns a Counter object.
    """
    return Counter(words)

# ==================== 5. Get top N words ====================
def get_top_words(counter, n=20):
    """
    Return the top N most frequent words.
    """
    return counter.most_common(n)

# ==================== 6. Save results to CSV ====================
def save_to_csv(counter, output_path):
    """
    Save word frequency results to a CSV file.
    """
    df = pd.DataFrame(counter.items(), columns=['Word', 'Frequency'])
    df = df.sort_values(by='Frequency', ascending=False)
    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"[SUCCESS] Results saved to: {output_path}")

# ==================== Main program ====================
def main():
    # Configuration
    input_file = "sample.txt"           ##### Please input your text file here. #####
    output_file = "word_frequency.csv"  ##### Results will be output through a CSV file under the same folder as the program file. #####
    top_n = 100                         ##### You may change the number of top frequent words to display here. #####

    # 1. Read text
    text = read_text(input_file)
    if text is None:
        return

    # 2. Clean text
    cleaned_text = clean_text(text)

    # 3. Tokenize
    words = tokenize(cleaned_text)
    token_count = len(words)                  
    print(f"[INFO] Token count (total words): {token_count}")

    # 4. Count frequency
    counter = count_word_frequency(words)
    type_count = len(counter)                  
    print(f"[INFO] Type count (unique words): {type_count}")
    print(f"[INFO] Type/Token ratio: {type_count/token_count:.2%}") 

    # 5. Display top words
    top_words = get_top_words(counter, top_n)
    print(f"\n[INFO] Top {top_n} most frequent words:")
    for word, freq in top_words:
        print(f"  {word}: {freq}")

    # 6. Save results
    save_to_csv(counter, output_file)

    print("[SUCCESS] Word frequency analysis complete!")

if __name__ == "__main__":
    main()
