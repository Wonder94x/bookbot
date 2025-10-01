import sys

def main():
    if len(sys.argv) == 1:
        print (f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    dict_list = sort_char_count(text)
    
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {file_path}...")
    print (f"----------- Word Count ----------")
    print (f"Found {word_count} total words")
    print (f"--------- Character Count -------")
    for i in dict_list:
        if i["char"].isalpha():
            print (f"{i["char"]}: {i["num"]}")
    print ("============= END ===============")
   


def get_book_text(path): # Function to get the full text of the book.
    with open(path) as f:
        book_text = f.read()
    return book_text


from stats import get_word_count

from stats import get_char_count

from stats import sort_char_count
    
main()