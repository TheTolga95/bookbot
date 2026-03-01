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

def sort_on(sorted_chars):
    return sorted_chars["num"]


def sort_characters(book_chars):
    sorted_chars = []

    for char in book_chars:
        char_count = {}
        char_count ["char"] = char
        char_count ["num"] = book_chars[char]
        sorted_chars.append(char_count)
    
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
    