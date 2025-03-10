import sys
from stats import count_words, count_each_char, sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main(book_name):
    print(get_book_text(book_name))

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
count_words(sys.argv[1])
count_each_char(sys.argv[1])
sorted_list(sys.argv[1])

print("============= END ===============")

