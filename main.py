from stats import get_word_count, get_book_text

def main():
    bookpath = "books/frankenstein.txt"
    booktext = get_book_text(bookpath)
    print(f"Found {len(get_word_count(booktext))} total words")
    return None

if __name__ == "__main__":
    main()