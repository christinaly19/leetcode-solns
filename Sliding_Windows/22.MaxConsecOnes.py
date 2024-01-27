# Problem 1004. Max Consecutive Ones III (Medium)
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # We want to keep at most 2 zeros in our "window", then we want to count the number of 1s to keep track of max so far 
        startingIndex = 0
        endingIndex = len(nums) - 1
        numZeros = 0
        maxConsec = 0
        for i in range(len(nums)):
            if numZeros == k:
                endingIndex = i
            if nums[i] == 0:
                numZeros = numZeros + 1
        currSet = Counter(nums[0:endingIndex])
        if (numZeros <= k):
            return len(nums)
        maxConsec = currSet[1] + currSet[0]
        while (endingIndex <= len(nums) - 1):
            if nums[endingIndex] == 0:
                while (nums[startingIndex] != 0):
                    currSet[1] = currSet[1] - 1
                    startingIndex = startingIndex + 1
                startingIndex = startingIndex + 1
            else:
                currSet[1] = currSet[1] + 1
            if (currSet[0] + currSet[1]) > maxConsec:
                maxConsec = currSet[1] + currSet[0]
            endingIndex = endingIndex + 1
        return maxConsec


            
'''
Debugging took some time :(
'''