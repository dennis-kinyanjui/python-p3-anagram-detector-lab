# your code goes here!# your code goes here!

# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        # Sort the letters of the initial word
        sorted_word = sorted(self.word)
        matches = []
        
        for word in word_list:
            if sorted(word) == sorted_word:
                matches.append(word)
        
        return matches