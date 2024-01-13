# 1652. Defuse the Bomb (Easy)
class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        answ = []
        if (k == 0):
            for i in range(len(code)):
                answ.append(0)
        
        if (k > 0):
            currK = 0
            j = 0
            totalSum = 0
            while (currK != k):
                if (j == len(code) - 1):
                    j = 0
                else:
                    j = j + 1
                totalSum = totalSum + code[j]
                currK = currK + 1
            answ.append(totalSum)
            ending = j
            for i in range(1, len(code)):
                baseSum = answ[i - 1] - code[i]
                if (j + 1 >= len(code)):
                    j = 0
                else:
                    j = j + 1
                sumToAdd = baseSum + code[j]
                answ.append(sumToAdd)
            print(answ)

        if (k < 0):
            index = len(code)
            currK = 0
            totalSum = 0
            while (currK != k * -1):
                if (index - 1 < 0):
                    index = len(code) - 1
                else:
                    index = index - 1
                totalSum = totalSum + code[index]
                currK = currK + 1
            j = index - 1
            answ.append(totalSum)
            for i in range(1, len(code)):
                if (j + 1 >= len(code)):
                    j = 0
                else:
                    j = j + 1
                addSum = answ[i - 1] - code[j] + code[i - 1]
                answ.append(addSum)
        return answ
'''
Should have used something like % for the circular array calculations...
'''