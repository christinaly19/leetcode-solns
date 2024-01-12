# 451. Sort Characters By Frequency (Medium)
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        lettersMap = {}
        for letter in s:
            lettersMap[letter] = lettersMap.get(letter, 0) + 1
        answ = ""
        while len(lettersMap) > 0:
            indexMax = max(lettersMap, key=lettersMap.get)
            stringAdd = ""
            for i in range(max(lettersMap.values())):
                stringAdd = stringAdd + indexMax
            answ = answ + stringAdd
            lettersMap.pop(indexMax)
        return answ