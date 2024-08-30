import pandas as pd
from collections import Counter
import re


# Read the file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# Count words
def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())  # Convert to lower and find words
    return Counter(words)  # Use Counter to count occurrences


# Count letters
def count_letters(text):
    letter_count = Counter(text.lower())  # Count all as lower
    upper_letter_count = Counter(filter(str.isupper, text))  # Count only upper

    # Prepare data for DataFrame
    total_letters = sum(letter_count.values())
    data = []
    for letter, count in letter_count.items():
        if letter.isalpha():  # Ensure we count only letters
            data.append({
                'letter': letter,
                'count_all': count,
                'count_uppercase': upper_letter_count[letter.upper()],
                'percentage': f"{(count / total_letters) * 100:.2f}%"
            })
    return data


def main():
    text = read_file('newsfeed.txt')  # Adjust path if needed

    # Get word count
    word_counts = count_words(text)
    words_df = pd.DataFrame(list(word_counts.items()), columns=['word', 'count'])
    words_df.to_csv('word_count.csv', index=False)

    # Get letter count
    letter_data = count_letters(text)
    letters_df = pd.DataFrame(letter_data)
    letters_df.to_csv('letter_count.csv', index=False)


if __name__ == "__main__":
    main()