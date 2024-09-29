def main():
    book_path = "books/frankenstein.txt"
    text = get_book_content(book_path)
    num_words = get_word_count(text)
    characters_dict = get_character_count(text)
    compiled = compile_report(characters_dict)
    print_report(book_path, num_words, compiled)  


def get_book_content(book_path):
    with open(book_path) as file:
        return file.read()    


def get_word_count(text):
    return len(text.split())


def get_character_count(text):
    character_count = {}

    for character in text.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count


def sort_on(dict):
    return dict["num"]


def compile_report(characters_dict):
    sorted = []
    for char in characters_dict:
        if char.isalpha():
            sorted.append({"c": char, "num" : characters_dict[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted


def print_report(book_path, num_words, compiled):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for char in compiled:
        print(f"The '{char['c']}' character was found {char['num']} times")

    print("--- End report ---")


main()

