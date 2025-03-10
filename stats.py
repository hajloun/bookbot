def get_book_text(book_name):
    with open(book_name) as f:
        file_contents = f.read()
        return file_contents

def count_words(book_name):
    words = get_book_text(book_name)
    word_count = len(words.split())
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

def count_each_char(book_name):
    word_dictionary = {}
    words = list(get_book_text(book_name).lower())
    for w in words:
        word_dictionary[w] = word_dictionary.get(w, 0) + 1
    return word_dictionary

def sorted_list(book_name):
    
    word_dictionary = count_each_char(book_name)
    sorted_dict = dict(sorted(
    ((k, v) for k, v in word_dictionary.items() if k.isalpha()),
    key=lambda item: item[1], 
    reverse=True
    ))
    print("--------- Character Count -------")
    for char, count in sorted_dict.items():
        print(f"{char}: {count}")
    