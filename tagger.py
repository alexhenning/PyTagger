import string, parser

lexicon = parser.parse("/home/alex/Dropbox/python/pos/pos.txt")

def tag(words):
    tags = [None for i in words]
    for i in range(len(words)):
        ss = lexicon.get(words[i], None)
        # 1/22/2002 mod (from Lisp code): if not in hash, try lower case:
        if not ss: ss = lexicon.get(words[i].lower(), None)
        if not ss and len(words[i]) == 1: tags[i] = words[i] + "^"
        if not ss: tags[i] = "NN"
        else: tags[i] = ss[0]

    # Apply transformational rules
    for i in range(len(words)):
        word = tags[i]
        
        # rule 1: DT, {VBD | VBP} --> DT, NN
        if i > 0 and tags[i-1] == "DT":
            if word == "VBD" or word == "VBP" or word == "VB":
                tags[i] = "NN"

        # rule 2: convert a noun to a number (CD) if "." appears in the word
        if word.startswith("N"):
            if "." in words[i]: tags[i] = "CD"
            # Attempt to convert into a number
            try:
                float(words[i])
                tags[i] = "CD"
            except ValueError: pass

        # rule 3: convert a noun to a past participle if words[i] ends with "ed"
        if tags[i].startswith("N") and words[i].endswith("ed"):
            tags[i] = "VBN"
        
        # rule 4: convert any type to adverb if it ends in "ly";
        if words[i].endswith("ly"):
            tags[i] = "RB"
            
        # rule 5: convert a common noun (NN or NNS) to adjective if it ends with "al"
        if tags[i].startswith("NN") and word.endswith("al"):
            tags[i] = "JJ"
            
        # rule 6: convert a noun to a verb if the preceding work is "would"
        if i > 0 and tags[i].startswith("NN") and words[i-1].lower() == "would":
            tags[i] = "VB"

        # rule 7: if a word has been categorized as a common noun and it ends with "s"
        #         then set its type to plural common noun (NNS)
        if tags[i] == "NN" and words[i].endswith("s"):
            tags[i] = "NNS"
            
        # rule 8: convert a common noun to a present participle verb (i.e., a gerund)
        if tags[i].startswith("NN") and words[i].endswith("ing"):
            tags[i] = "VBG"

    return zip(words, tags)
