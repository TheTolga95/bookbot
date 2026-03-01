def get_book_text(bookpath):
    contents = ""
    with open(bookpath) as content:
        contents =  content.read()
    return contents

def get_word_count(booktext):
    return booktext.split()

def main():
    bookpath = "books/frankenstein.txt"
    booktext = get_book_text(bookpath)
    print(f"Found {len(get_word_count(booktext))} total words")
    return None

if __name__ == "__main__":
    main()