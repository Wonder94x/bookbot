def get_word_count(text): # Function to get the number of words in the book's text.
    words = text.split()
    return len(words)


def get_char_count(text): # Function to count the how many times each single character is repeated in a dictionary format.

    char_list = list(text.lower()) # convert the into single characters all in lower case
    char_dict = {}

    for c in char_list:
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    
    return char_dict


def sort_char_count (text): # Function to sort character count from highest to lowest count.

    dict_list = []
    char_dict = get_char_count(text)

    for char, num in char_dict.items():
        dict_pair = {}
        dict_pair["char"] = char 
        dict_pair["num"] = num
        dict_list.append(dict_pair)        
    
    return sorted(dict_list, key=lambda x: x["num"], reverse=True)





