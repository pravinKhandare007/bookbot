def count_number_of_words(text):
    word_array = text.split()
    return len(word_array)

def char_count(text):
    char_dict = {}
    for char in text.lower():
        if(char in char_dict):
            char_dict[char] += 1 
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def sort_dict(dictionary):
    array_of_dict = []
    for key in dictionary:
        array_of_dict.append({"char_name": key , "count": dictionary[key]})
    array_of_dict.sort(reverse = True, key=sort_on)
    return array_of_dict
