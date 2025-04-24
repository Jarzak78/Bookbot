def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    text = text.lower()  # Convert all characters to lowercase
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def chars_dict_to_sorted_list(char_count):
    chars_list = []

    for char, count in char_count.items():
        chars_list.append({"char" : char,"num" : count})
    
    chars_list.sort(reverse=True, key=lambda d: d["num"])

    return chars_list

  
