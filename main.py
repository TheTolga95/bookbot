import sys
from stats import get_word_count, get_book_text, count_characters, sort_characters

def main():
    print("Usage: python3 main.py <path_to_book>")
    if len(sys.argv) != 2:
        sys.exit(1)

    bookpath = sys.argv[1]
    booktext = get_book_text(bookpath)
    word_count = get_word_count(booktext)
    counted_characters = count_characters(booktext)
    sorted_characters = sort_characters(counted_characters)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print(f"----------- Word Count ----------")
    print(f"Found {len(get_word_count(booktext))} total words")
    print(f"----------- Character Count ----------")
    for char in sorted_characters:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
    print(f"============= END ===============")


    return None

if __name__ == "__main__":
    main()