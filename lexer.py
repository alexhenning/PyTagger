import re

endings = "!.,?;:"
def lex(s):
    raw_words = s.split(" ")
    words = []
    for word in raw_words:
        if word[-1] in endings:
            words.extend([word[:-1], word[-1]])
        else:
            words.append(word)
    return words
