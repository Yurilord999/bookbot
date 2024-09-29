def main():
    text = get_content()
    print(text)
    print(get_word_count())    

def get_content():
    with open("books/frankenstein.txt") as file:
        return file.read()    

def get_word_count():
    words = get_content().split()
    return len(words)

main()

