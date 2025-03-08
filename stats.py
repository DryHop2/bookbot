def count_words(text):
    return len(text.split())


def count_characters(text):
    lowered_string = text.lower()
    count_dict = {}
    for c in lowered_string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    return count_dict

def sort_on(dict):
    return dict["num"]


# def dict_to_sorted_list(count_chars_dict):
#     letters = []
#     for k, v in count_chars_dict.items():
#         if k.isalpha():
#             letters.append({"letter": k, "count": v}) 
#     letters.sort(reverse=True, key=sort_on)
#     return letters


def dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list