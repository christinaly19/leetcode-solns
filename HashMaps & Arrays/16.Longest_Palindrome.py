# 409. Longest Palindrome (easy)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        lettersMap = {}
        for letter in s:
            lettersMap[letter] = lettersMap.get(letter, 0) + 1
        count = 0
        allowOne = True
        if len(lettersMap) == 1:
            for key in lettersMap:
               return lettersMap[key]
        for key in lettersMap:
            if (lettersMap[key] % 2 == 0):
                count = count + lettersMap[key]
            else:
                if (allowOne == True):
                    allowOne = False
                    count = count + lettersMap[key]
                else:
                    count = count + (lettersMap[key] - 1)
    
        return count

