from os.path import exists


def read_line(n, file):
    if not isinstance(n, int):
        return "invalid input detected"
    if not exists(file):
        return "file not found"
    lines = []
    with open(file) as f:
        lines = f.readlines()
    if n >= len(lines):
        f.close()
        return "line " + str(n) + " doesn't exist"
    f.close()
    return lines[n-1]


def is_longer(word, words):
    n = len(word)
    i = 0
    while i < 5 and i < len(words):
        if len(words[i]) < n:
            words.insert(i, word)
            if len(words) > 5:
                words.remove(words[5])
            return
        i += 1


def longest_words(file):
    if not isinstance(file, str) or not exists(file):
        print("file not found")
        return []
    words = []
    with open(file, 'r') as f:
        special_characters = list("!@# $%^&*()-+?_=,<>/")
        my_file = f.read()
        words = [''.join(c for c in s if c.isalpha()) for s in my_file.split()]
        arr = sorted(words, key=len)
        print(arr)
    return arr[len(arr) - 5:]

