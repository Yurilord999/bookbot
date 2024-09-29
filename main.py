def main():
    text = get_content()
    words = get_word_count()
    characters = get_character_count()
    print(text)
    print(words)
    print(characters)    

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
main()

