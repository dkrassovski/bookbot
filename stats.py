def get_book_text (path):
    with open(path) as f:
        return f.read()
def number_of_words():
    book_text = get_book_text("books/frankenstein.txt")
    book_text = book_text.split()
    num_words = len(book_text)
    print (f"{num_words} words found in the document")

def count ():
    book_text = get_book_text("books/frankenstein.txt")
    book_text = book_text.lower()
    letter_count = {}
    for letter in book_text:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count
def sorted_letters(letter_count):
    sorted_data = sorted([{"character": char, "count": count} for char, count in letter_count.items()], key=lambda x: x["count"], reverse=True)
    return sorted_data
def print_report():
    print ("============ BOOKBOT ============")
    print ("Analyzing book found at books/frankenstein.txt...")
    print ("----------- Word Count ----------")
    number_of_words()
    print ("--------- Character Count -------")
    letter_count = count()
    sorted_data = sorted_letters(letter_count)
    for item in sorted_data:
        print(f"{item['character']}: {item['count']}")
    print ("============= END ===============")
print_report()