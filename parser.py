
def parse(path):
    lexicon = {}
    with file(path, "r") as f:
        for line in f:
            word, pos = [i.strip(" \n") for i in line.split("::")]
            lexicon[word] = pos.split(" ")
    return lexicon
            
