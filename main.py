import sys
from stats import counting
from stats import sort_desc

def sys_import():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    return book_path

def get_book_text(filepath):
    print("============ BOOKBOT ============")
    print("Analyzing book found at "+filepath+"...")
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = sys_import()
    book_text = get_book_text(book_path)
    #stats.py
    count_by_character = counting(book_text)
    sort_desc(count_by_character)

main()