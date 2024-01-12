#13. Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        orderMap = {'I': 1, 'V': 2, 'X': 3, 'L': 4, 'C': 5, 'D': 6, 'M': 7}
        valuesMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sumSoFar = 0
        for i in range(len(s)):
            if (i == len(s) - 1):
                sumSoFar = sumSoFar + valuesMap[s[i]]
            else:
                if orderMap[s[i]] < orderMap[s[i+1]]:
                    sumSoFar = sumSoFar - valuesMap[s[i]]
                else:
                    sumSoFar = sumSoFar + valuesMap[s[i]]
        return sumSoFar
    