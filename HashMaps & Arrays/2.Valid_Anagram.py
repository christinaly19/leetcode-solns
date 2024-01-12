#242. Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lettersMap1 = {}
        lettersMap2 = {}
        for letter in s:
            if letter in lettersMap1:
                lettersMap1[letter] = lettersMap1.get(letter) + 1
            else:
                lettersMap1[letter] = 1
        
        for letter in t:
            if letter in lettersMap2:
                lettersMap2[letter] = lettersMap2.get(letter) + 1
            else:
                lettersMap2[letter] = 1

        return (lettersMap1 == lettersMap2)
    
'''
Probably not the best possible solution; can also just have 1 hashmap, and for t, decrease (-1) value for each key
and loop through hashmap to ensure all values are 0 to return true.
'''