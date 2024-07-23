def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = word_count(text)
    lowered_text = lower_case(text)
    lowered_dict = letter_count(lowered_text)
    sorted_dict_list = list_of_dicts(lowered_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{total_words} words were found in the document")
    print()

    for item in sorted_dict_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

def list_of_dicts(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_dict)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(s):
    words = len(s.split())
    return words

def lower_case(words):
    lowered = words.lower()
    return lowered

def letter_count(s):
    d = {}
    for i in s:
        if i.isalpha():
            d[i] = d.get(i,0) + 1 
    return d

def sort_dict(dict):
    return dict["num"]

main()