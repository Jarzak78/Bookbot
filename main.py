import sys

from stats import character_count
from stats import get_num_words
from stats import chars_dict_to_sorted_list


def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

     
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
 
    filepath = sys.argv[1]

    try:
        book_text = get_book_text(filepath) # Read the book text
        num_words = get_num_words(book_text) # Print the number of words
        char_count = character_count(book_text) # Count the characters
        sorted_list = chars_dict_to_sorted_list(char_count) # Sort the characters
        
        #print the report
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char_dict in sorted_list:
            char = char_dict["char"]
            count = char_dict["num"]
            if char.isalpha():
                print(f"{char}: {count}")
        print("============= END ===============")

    except FileNotFoundError:

        print(f"File not found: {filepath}")
        sys.exit(1)




if __name__ == "__main__":
    main()