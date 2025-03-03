from stats import count_number_of_words,char_count,sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

def main():
    arguments = sys.argv

    if len(arguments) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_content = get_book_text(arguments[1])
    number = count_number_of_words(file_content)
    char_dict = char_count(file_content)
    print(f'''============ BOOKBOT ============
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------
    Found {number} total words
    --------- Character Count -------
    ''')
    sorted_array_of_dictionary = sort_dict(char_dict)
    for d in sorted_array_of_dictionary:
        print(f'{d["char_name"]}: {d["count"]}')
    print("============= END ===============")

main()