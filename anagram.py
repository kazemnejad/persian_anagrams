from itertools import permutations

words = set()


def read_words():
    wordsFile = open("dataset.txt", "r")
    for line in wordsFile:
        words.add(line[:-1])


def anagrams(word):
    for perm in permutations(word):
        perm = ''.join(perm)
        if perm in words:
            yield perm


def main_loop():
    while (True):
        word = input(
            "Enter a word to find its Anagrams (Press Enter to exit)\n")
        if word == "":
            break

        print("[  ", end="")
        for anagram in anagrams(word):
            print(anagram, end="  ")
        print("]\n")


if __name__ == "__main__":
    read_words()
    main_loop()
