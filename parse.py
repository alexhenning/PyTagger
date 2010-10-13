
posTokens = ["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS", "MD", "NN", "NNP", "NNPS", "NNS", "POS", "PDT", "PP$", "PRP", "RB", "RBR", "RBS", "RP", "SYM", "TO", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB", ",", ".", ":", "$", "#", '"', "(", ")"]


to_strip = '" \t[:\n,]'

f = file("pos.js", "r")
out = file("pos.txt", "w")

words = []

word = None
pos = []

for line in f:
    line = line.strip(to_strip)
    if "|" in line: pass
    elif line in posTokens: words[-1][1].append(line)
    elif line: words.append([line, []])
#    print len(words), words[-1]
f.close()
    
for word, pos in words:
    out.write("%s :: %s\n"%(word, " ".join(pos)))
out.close()
