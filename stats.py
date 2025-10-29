def count_words(book_text):
    words = book_text.split()
    count = len(words)
    print(f"Found {count} total words")

def count_characters(book_text):
    character = {}
    full_text = book_text.lower()
    for text_character in full_text:
        if text_character in character:
            character[text_character] += 1
        else:
            character[text_character] = 1
    return character
