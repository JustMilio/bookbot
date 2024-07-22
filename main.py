def main():
    # with open("books/frankenstein.txt") as f:
    #     file_contents = f.read()
    #     print(file_contents)
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count(text)
    # print(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(s):
    words = len(s.split())
    print(words)
    return words


main()