def counting(book_text):
    print("----------- Word Count ----------")
    words = book_text.split()
    count = len(words)
    print(f"Found {count} total words")

    print("--------- Character Count -------")
    character = {}
    full_text = book_text.lower()
    for text_character in full_text:
        if text_character in character:
            character[text_character] += 1
        else:
            character[text_character] = 1
    return character

def sort_func(chars):
    return chars["num"]

def sort_desc(characters):
    sorted_chars = []
    for character in characters:
        character_set = {
            "char": character,
            "num": characters[character],
            }
        sorted_chars.append(character_set)
    sorted_chars.sort(reverse=True, key=sort_func)

    for sorted_char in sorted_chars:
        if sorted_char["char"].isalpha():
            print(f"{sorted_char["char"]}: {sorted_char["num"]}")
    print("============= END ===============")