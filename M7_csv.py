import csv
from collections import Counter
import re

# Read the file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Count words
def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())  # Convert all text to lowercase and find words
    return Counter(words)  # Use Counter to count occurrences

# Count letters
def count_letters(text):
    letter_count = Counter(text.lower())  # Count each character in lowercase
    upper_letter_count = Counter(filter(str.isupper, text))  # Count only uppercase characters

    total_letters = sum(letter_count.values())
    data = []
    for letter, count in letter_count.items():
        if letter.isalpha():  # Make sure to only count alphabetic characters
            upper_count = upper_letter_count[letter.upper()]
            percentage = (count / total_letters) * 100
            data.append([letter, count, upper_count, f"{percentage:.2f}%"])
    return data

def main():
    text = read_file('newsfeed.txt')  # Adjust the file path as needed

    # Word counts
    word_counts = count_words(text)
    with open('word_count.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['word', 'count'])  # writing headers
        for word, count in word_counts.items():
            writer.writerow([word, count])

    # Letter counts
    letter_data = count_letters(text)
    with open('letter_count.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['letter', 'count_all', 'count_uppercase', 'percentage'])
        for row in letter_data:
            writer.writerow(row)

if __name__ == "__main__":
    main()