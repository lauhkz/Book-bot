def main():
    text = read_book()
    #print(text)
    count_words(text)
    dict_of_chars = count_characters(text)
    print(dict_of_chars)

def read_book():
    with open("books/frankenstein.txt") as f:
        return f.read()

def count_words(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    print(f"There is a total of {counter} words in this book")

def count_characters(text):
    text_to_lowercase = text.lower()
    characters = {
        "a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0,
        "f":0,
        "g":0,
        "h":0,
        "i":0,
        "j":0,
        "k":0,
        "l":0,
        "m":0,
        "n":0,
        "o":0,
        "p":0,
        "q":0,
        "r":0,
        "s":0,
        "t":0,
        "u":0,
        "v":0,
        "w":0,
        "x":0,
        "y":0,
        "z":0,
    }
    for word in text_to_lowercase:
        if word == "a":
            characters['a'] += 1
        elif word == "b":
            characters['b'] += 1
        elif word == "c":
            characters['c'] += 1
        elif word == "d":
            characters['d'] += 1
        elif word == "e":
            characters['e'] += 1
        elif word == "f":
            characters['f'] += 1
        elif word == "g":
            characters['g'] += 1
        elif word == "h":
            characters['h'] += 1
        elif word == "i":
            characters['i'] += 1
        elif word == "j":
            characters['j'] += 1
        elif word == "k":
            characters['k'] += 1
        elif word == "l":
            characters['l'] += 1
        elif word == "m":
            characters['m'] += 1
        elif word == "n":
            characters['n'] += 1
        elif word == "o":
            characters['o'] += 1
        elif word == "p":
            characters['p'] += 1
        elif word == "q":
            characters['q'] += 1
        elif word == "r":
            characters['r'] += 1
        elif word == "s":
            characters['s'] += 1
        elif word == "t":
            characters['t'] += 1
        elif word == "u":
            characters['u'] += 1
        elif word == "v":
            characters['v'] += 1
        elif word == "w":
            characters['w'] += 1
        elif word == "x":
            characters['x'] += 1
        elif word == "y":
            characters['y'] += 1
        elif word == "z":
            characters['z'] += 1
    return characters


main()
