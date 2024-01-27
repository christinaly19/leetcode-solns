# 24: Longest Common Prefix (easy)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longestCommon = []
        length = len(strs[0])
        currIndex = 0
        if len(strs) == 1:
            return strs[0]
        for i in range(length):
            for word in strs[1::]:
                if i >= len(word) or word[i] != strs[0][i]:
                    return ''.join(longestCommon)
            longestCommon.append(word[i])
        return ''.join(longestCommon)

        