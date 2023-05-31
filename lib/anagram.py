

class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, match):
        return [w for w in match if sorted(w) == sorted(self.word)]