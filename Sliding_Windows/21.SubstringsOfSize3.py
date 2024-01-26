# Question 1876 Substrings of Size Three with Distinct Characters (Easy)

class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        lettersCount = Counter(s[0])
        totalOccur = 0
        for i in range(1, len(s)):
            lettersCount[s[i]] = lettersCount[s[i]] + 1
            if (i >= 3):
                lettersCount[s[i-3]] = lettersCount[s[i-3]] - 1
                if (lettersCount[s[i-3]] == 0):
                    lettersCount.pop(s[i-3])
            if (i >= 2):
                if (len(lettersCount) == 3):
                    totalOccur = totalOccur + 1
                
            
        
        return totalOccur
