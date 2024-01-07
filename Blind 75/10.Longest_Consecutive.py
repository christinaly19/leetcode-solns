# 128. Longest Consecutive Sequence
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longestSoFar = 0
        # remove the duplicates in the nums 
        nums_set = set(nums) 

        for num in nums_set:
            if (num - 1) not in nums_set:
                # this means it is the first number of a streak
                checkNum = num
                currStreak = 1
                while (checkNum + 1) in nums_set:
                    currStreak = currStreak + 1
                    checkNum = checkNum + 1
                if currStreak > longestSoFar:
                    longestSoFar = currStreak
        
        return longestSoFar
    
    '''
    Need to use set(nums) to remove the duplicates of values in the nums array
    Steps through the array, checking each possible "start" for their longest streak 
    '''

        