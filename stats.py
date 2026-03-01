def get_book_text(bookpath):
    contents = ""
    with open(bookpath) as content:
        contents =  content.read()
    return contents

def get_word_count(booktext):
    return booktext.split()