from stats import count_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    #print(book_text)
    count_words(book_text)
    count_by_character = count_characters(book_text)
    print(count_by_character)

main()