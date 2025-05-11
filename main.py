import sys
from stats import count_words, count_chars, report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    num_words = count_words(book)
    chars = count_chars(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(report(chars))

    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


main()
