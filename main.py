def main():
    text = get_content()
    words = get_word_count()
    characters = get_character_count()
    compiled = compile_report(characters)
    print_report(words, compiled)  

def get_content():
    with open("books/frankenstein.txt") as file:
        return file.read()    

def get_word_count():
    words = get_content().split()
    return len(words)

def get_character_count():
    character_count = {}
    text = get_content().lower().split()

    for word in text:
        for character in word:
            if character in character_count:
                character_count[character] += 1
            elif character not in character_count:
                character_count[character] = 1

    return character_count

def sort_on(dict):
    return dict["num"]

def compile_report(characters):
    sorted = []
    for char in characters:
        if char.isalpha():
            sorted.append({"c": char, "num" : characters[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

def print_report(words,compiled):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print("")
    for char in compiled:
        print(f"The '{char['c']}' character was found {char['num']} times")

    print("--- End report ---")
main()

