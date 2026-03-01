def get_book_text(bookpath):
    contents = ""
    with open(bookpath) as content:
        contents =  content.read()
    return contents

def get_word_count(booktext):
    return booktext.split()

def count_characters(booktext):
    booktext = booktext.lower()
    characters = {}

    for character in range(0,len(booktext)):
        if booktext[character] not in characters:
            characters[booktext[character]] = 1
        else:
            characters[booktext[character]] += 1
    return characters