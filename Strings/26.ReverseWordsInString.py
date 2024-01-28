# 151: Reverse Words in String (medium)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        end = len(s) - 1
        newWord = []
        while end >= 0:
            if s[end] != " ":
                newWord.append(s[end])
                print(newWord)
            elif s[end] == " ":
                if len(newWord) > 0:
                    words.append("".join(newWord[::-1]))
                newWord = []
            # last (first) word
            if end == 0:
                if len(newWord) > 0:
                    words.append("".join(newWord[::-1]))
            end = end - 1
        return " ".join(words)
   
'''
Mostly ok. horrific runtime tho
'''