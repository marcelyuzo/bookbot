import sys
from stats import count_words
from stats import count_characters
from stats import sort_list

if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    characters = count_characters(text)
    sorted = sort_list(characters)
    print(f"============ BOOKBOT ============\nAnalyzing book found at "+ path + f"...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    for dictionary in sorted:
        if dictionary["char"].isalpha():
            print(dictionary["char"]+f": {dictionary["num"]}")
    print("============= END ===============")

main()