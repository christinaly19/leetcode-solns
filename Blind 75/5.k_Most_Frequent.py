# 347. Top K Frequent Elements
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqMap = {}
        for n in nums:
            if n in freqMap:
                freqMap[n] = freqMap.get(n) + 1
            else:
                freqMap[n] = 1
        answ = []
        for x in range(k):
            highestVal = max(freqMap.values())
            for i, n in freqMap.items():
                if n == highestVal:
                    answ.append(i)
                    freqMap[i] = 0
                    break

        return answ
'''
Soln: Another hashmap! basically counted the occurence of all nums in the array, and then used max to find the k most frequent.
'''