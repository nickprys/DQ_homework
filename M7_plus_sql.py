import csv
from collections import Counter
import re
from M10v3 import DatabaseManager  # Import the DatabaseManager class


# Read the file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# Count words
def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)


# Count letters
def count_letters(text):
    letter_count = Counter(text.lower())
    upper_letter_count = Counter(filter(str.isupper, text))
    total_letters = sum(letter_count.values())
    data = []
    for letter, count in letter_count.items():
        if letter.isalpha():
            upper_count = upper_letter_count[letter.upper()]
            percentage = (count / total_letters) * 100
            data.append([letter, count, upper_count, f"{percentage:.2f}%"])
    return data


def main():
    db_manager = DatabaseManager("test2.db")  # Database file
    text = read_file('newsfeed.txt')

    # Word counts
    word_counts = count_words(text)
    for word, count in word_counts.items():
        db_manager.insert_word_count(word, count)

    # Letter counts
    letter_data = count_letters(text)
    for letter, count_all, count_upper, percentage in letter_data:
        db_manager.insert_letter_count(letter, count_all, count_upper, percentage)


if __name__ == "__main__":
    main()