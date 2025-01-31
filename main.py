def main():
    print_report(book)

def read_book(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(text):
    count = len(text.split())
    return count

def count_characters(text):
    characters = {}
    for letter in text:
        characters.setdefault(letter.lower(), 0)
        characters[letter.lower()] += 1
    return characters

def get_alphabet(text):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alpha_char = {}
    for letter in all_characters:
        if letter in alphabet:
            alpha_char[letter] = all_characters[letter]
    return alpha_char

def print_report(text):
    print(f"""
    --- Begin report of books/frankenstein.txt ---
    {words} words found in the document
    """)
    for item in alpha_characters:
        print(f"The '{item}' character was found {alpha_characters[item]} times")
    print("--- End report ---")
    return

book = read_book("books/frankenstein.txt")
words = count_words(book)
all_characters = count_characters(book)
alpha_characters = get_alphabet(book)

main()




