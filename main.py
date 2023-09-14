def wordCount(string):
    return len(string.split())


def letterCount(string):
    words = string.lower().split()
    wc = {}
    for word in words:
        for letter in word:
            wc.setdefault(letter, 0)
            if wc[letter] >= 0:
                wc[letter] += 1
    return wc


def printReport(string, file):
    file_name = file.split("/").pop()
    letter_count = letterCount(string)
    sorted_letters = sorted(list(letter_count))
    print(f"__ Report of book {file_name}__")
    print(f"{wordCount(string)} words found in the document.\n")
    for letter in sorted_letters:
        if letter.isalpha():
            print(
                f"The '{letter}' character was found {letter_count[letter]} times. \n "
            )

        else:
            continue
    print("___End Report___")


with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    printReport(file_contents, "/books/frankenstein.txt")
