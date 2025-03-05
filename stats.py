def get_book_text (path):
    with open(path) as f:
        return f.read()
def main():
    book_text = get_book_text("books/frankenstein.txt")
    book_text = book_text.split()
    num_words = 0
    for i in range(len(book_text)):
        num_words = i + 1
    print (f"{num_words} words found in the document")

def count ():
    book_text = get_book_text("books/frankenstein.txt")
    book_text = book_text.lower()
    letter_count = {}
    for letter in book_text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    print (letter_count) 

main() 
count()