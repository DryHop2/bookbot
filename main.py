import sys
from stats import (count_words,
                   count_characters,
                   dict_to_sorted_list)


def main():
    # path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]

    text = get_text(path)
    num_words = count_words(text)
    chars_dict = count_characters(text)
    sorted_char_list = dict_to_sorted_list(chars_dict)
    print_report(path, num_words, sorted_char_list)

    # print(f"--- Begin report of {path} ---")
    # print(f"{num_words} words found in the document")
    # print()

    # for char in sorted_char_list:
    #     print(f"The '{char['letter']}' character was found {char['count']} times.")
        
    # print("--- End Report ---")

def get_text(path):
    with open(path) as f:
        return f.read()

# def count_words(text):
#     return len(text.split())

# def count_characters(text):
#     lowered_string = text.lower()
#     count_dict = {}
#     for c in lowered_string:
#         if c in count_dict:
#             count_dict[c] += 1
#         else:
#             count_dict[c] = 1
#     return count_dict

# def sort_on(dict):
#     return dict["count"]

# def dict_to_sorted_list(count_chars_dict):
#     letters = []
#     for k, v in count_chars_dict.items():
#         if k.isalpha():
#             letters.append({"letter": k, "count": v}) 
#     letters.sort(reverse=True, key=sort_on)
#     return letters

def print_report(path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()