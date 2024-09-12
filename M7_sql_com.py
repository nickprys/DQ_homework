import csv
from collections import Counter
import re
from M10v3 import DatabaseManager  # Import the DatabaseManager class which handles database operations.


# Function to read a raw text from a file.
def read_file(file_path):
    # Open the file in read mode.
    with open(file_path, 'r') as file:
        # Read and return the entire file content.
        return file.read()


# Function to count the occurrences of each distinct word in the text.
def count_words(text):
    # Find all words using regular expression, converting the text to lowercase to ensure case-insensitivity.
    words = re.findall(r'\b\w+\b', text.lower())
    # Return a dictionary counting occurrences of each word.
    return Counter(words)


# Function to count the occurrences and percentage of each letter in the text.
def count_letters(text):
    # Count characters in all lowercase (to be case-insensitive) and calculate occurrences.
    letter_count = Counter(text.lower())
    # Count only uppercase characters to calculate how many of them appear upper-cased.
    upper_letter_count = Counter(filter(str.isupper, text))
    # Sum of all alphabetically counted letters (used for percentage calculation).
    total_letters = sum(letter_count.values())
    data = []
    for letter, count in letter_count.items():
        if letter.isalpha():  # Ensure only alphabet characters are considered.
            upper_count = upper_letter_count[letter.upper()]
            percentage = (count / total_letters) * 100
            # Collect letter data in a list of lists.
            data.append([letter, count, upper_count, f"{percentage:.2f}%"])
    return data


def main():
    # Initialize database manager with specific database path.
    db_manager = DatabaseManager("test2.db")

    # Load and process text data from file.
    text = read_file('newsfeed.txt')

    # Counting words and inserting them into the database.
    word_counts = count_words(text)
    for word, count in word_counts.items():
        # Each word and its count is stored in the database.
        db_manager.insert_word_count(word, count)

    # Counting letters and inserting them into the database.
    letter_data = count_letters(text)  # Corrected from count_letter to count_letters(text)
    for letter, count_all, count_upper, percentage in letter_data:
        # Each letter with its count, uppercase count, and percentage is stored.
        db_manager.insert_letter_count(letter, count_all, count_upper, percentage)


# Ensuring the script runs only when directly executed (not imported).
if __name__ == "__main__":
    main()


# Ensuring the script runs only when directly executed (not imported).
if __name__ == "__main__":
    main()