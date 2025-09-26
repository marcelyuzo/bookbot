def count_words(text):
    list_of_words = text.split() 
    num_words = len(list_of_words)
    return num_words

def count_characters(text):
    lower_case_text = text.lower()
    dictionary = {}
    for letter in lower_case_text:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    return dictionary

def sort_on(items):
    return items["num"]

def sort_list(dictionary):
    sorted_list = []
    for key in dictionary:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = dictionary[key]
        sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
