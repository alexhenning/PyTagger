import re

endings = "!.,?;:"
def lex(s):
    raw_words = [i for i in [j.strip(" ()\n\t") for j in s.split(" ")] if i]
    words = []
    for word in raw_words:
        if word[-1] in endings:
            words.extend([word[:-1], word[-1]])
        else:
            words.append(word)
    return words
