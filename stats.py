
def count_words(document):
    splitted = document.split()
    return len(splitted)

def count_chars(document):
    words = document.lower().split()
    letter_counter = dict()
    for word in words:
        for letter in word:
            if letter not in letter_counter:
                letter_counter[letter] = 0
            letter_counter[letter] += 1 
    return letter_counter

def sort_on(dct):
    return dict(sorted(dct.items(), key=lambda x: x[1], reverse=True))

    
def report(dictionary):
    tst = dictionary.copy()
    sorted_dict = sort_on(tst)
    for k, v in sorted_dict.items():
        print(f"{k}: {v}")

