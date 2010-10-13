
import sys, random
sys.path.append("../..")

from pos import tag, lex

parts_of_speech = {"CD": "a number",
                   "FW": "a foreign sounding word",
                   "IN": "a prepostition",
                   "JJ": "an adjective",
                   "JJR": "a comparative adjective",
                   "JJS": "a superlative adjective",
                   "NN": "a noun",
                   "NNP": "a proper noun",
                   "NNPS": "a proper plural noun",
                   "NNS": "a plural noun",
                   "RB": "an adverb",
                   "RBR": "a comparative adverb",
                   "RBS": "a superlative adverb",
                   "UH": "an interjection",
                   "VB": "a verb",
                   "VBD": "a verb in the past tense",
                   "VBG": "a gerund",
                   "VBN": "a past participle verb",
                   "VBP": "a present tense verb",
                   "VBZ": "a present tense verb"}

class Madlib(object):
    def __init__(self, text, blanks=2):
        self.numBlanks = blanks
        self.text = tag(lex(text))
        self.blanks = []
        self.get_blanks()
        self.indx = 0
        self.answers = []

    def get_blanks(self):
        while len(self.blanks) < self.numBlanks:
            indx = random.choice(self.text)
            if indx[1] in parts_of_speech.keys() and \
                    self.text.index(indx) not in self.blanks:
                self.blanks.append(self.text.index(indx))
        self.blanks.sort()
        
    def next(self):
        if self.indx < len(self.blanks):
            return parts_of_speech[self.text[self.blanks[self.indx]][1]]
        else:
            None
    def answer_next(self, answer):
        if self.indx < len(self.blanks):
            self.answers.append(answer)
            self.indx += 1
        
    def __str__(self, ):
        t = [i[0] for i in self.text]
        for i in range(len(self.blanks)):
            t[self.blanks[i]] = self.answers[i]
        return " ".join(t)

if __name__ == "__main__":
    m = Madlib("People are often surprised, somtimes astounded at the skill he excersized. He could run, walk, sleep and even talk!", 4)
    m = Madlib("""The Cylon War is long over, yet we must not forget the reasons why so many sacrificed so much in the cause of freedom. The cost of wearing the uniform can be high ... [after looking at crowd] but sometimes it's too high.
You know, when we fought the Cylons, we did it to save ourselves from extinction. But we never answered the question, why? Why are we as a people worth saving? We still commit murder because of greed, spite, jealousy. And we still visit all of our sins upon our children. We refuse to accept the responsibility for anything that we've done. Like we did with the Cylons. We decided to play God, create life. When that life turned against us, we comforted ourselves in the knowledge that it really wasn't our fault, not really. You cannot play God then wash your hands of the things that you've created. Sooner or later, the day comes when you can't hide from the things that you've done anymore.""", 10)
    """After the war the army was scraping the bottom of the barrel to get the guys for the occupation forces in Germany. Up until then the army
deferred people for some reason other than physical first (I was deferred because I was working on the bomb), but now they reversed that and gave
everybody a physical first."""
    s="""

That summer I was working for Hans Bethe at General Electric in Schenectady, New York, and I remember that I had to go some distance-I
think it was to Albany--to take the physical.

I get to the draft place, and I'm handed a lot of forms to fill out, and then I start going around to all these different booths. They check your vision
at one, your hearing at another, they take your blood sample at another, and so forth.

Anyway, finally you come to booth number thirteen: psychiatrist. There you wait, sitting on one of the benches, and while I'm waiting I can see
what is happening. There are three desks, with a psychiatrist behind each one, and the "culprit" sits across from the psychiatrist in his BVDs and
answers various questions."""
    print ""
    while m.next() != None:
        m.answer_next(raw_input("Please give me %s. "%m.next()))

    print ""
    print m
