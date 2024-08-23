def main():
    text = read_book()
    count_words(text)
    #print(text)

def read_book():
    with open("books/frankenstein.txt") as f:
        return f.read()

def count_words(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

main()
