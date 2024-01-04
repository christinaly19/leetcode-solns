#890. Find and Replace Pattern (Medium)
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        # create a hash for the pattern 
        answ = []
        for word in words:
            lettersHash = {}
            for i, letter in enumerate(word):
                if (letter not in lettersHash and pattern[i] not in lettersHash.values()):
                    lettersHash[letter] = pattern[i]
                elif letter not in lettersHash:
                    lettersHash[letter] = "_"
            newWord = list(word)
            for i, letter in enumerate(word):
                newWord[i] = lettersHash[word[i]]
            newWord = "".join(newWord)
            if newWord == pattern:
                answ.append(word)
        return answ
'''
Use a hashmap indicating which each value should map to in string pattern; and then mapping it to determine if we end up with the same pattern.
Ensure no key gets mapped to the same value in 
Here, _ represents that mapping is unsuccessful... could just skip and continue the loop here, for efficiency
'''