# bookbot

from stats import get_book_text, word_count, char_count, lister, printer
import sys

def main():

    try:
        path = sys.argv[1] 
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(path)
    count = word_count(text)
    chars = char_count(text)
    dictlist = lister(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    printer(dictlist)

main()
