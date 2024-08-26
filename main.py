def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    # print(text)
    total = count_words(text)

    # Here is the fuzzy and noisy stuff
    all_chars = count_characters(text)

    only_alpha = get_alpha(all_chars)

    report(only_alpha, total, path)


# TODO
def report(chars, total_words, path):
    print(f"--- Begin report of {path} ---")
    print(f"{total_words} words found in the document")
    print("")
    for key in chars:
        print(f"The '{key[0]}' character was found {key[1]} times")
    print("--- End report ---")


# Returns the all text
def read_book(path):
    with open(path) as f:
        return f.read()


# Returns the total of "words" in the text
def count_words(text):
    words = text.split()
    return len(words)


def get_alpha(lst):
    sorted_list = lst
    alpha_list = {}
    for key in sorted_list[0]:
        if key.isalpha():
            alpha_list[key] = sorted_list[0].get(key)

    alpha_list = list(alpha_list.items())
    items = sorted(alpha_list, reverse=True, key=lambda char: char[1])

    return items


# Returns a list with the count of each character in the text
def count_characters(text):
    text_to_lowercase = text.lower()
    characters = {}
    characters_list = []

    for word in text_to_lowercase:
        if word in characters:
            characters[word] += 1
        else:
            characters[word] = 1
    characters_list.append(characters)
    return characters_list


main()
