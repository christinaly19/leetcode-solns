# Question 1: Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        checked = {}
        for i, n in enumerate(nums):
            lookFor = target - n
            if lookFor in checked:
                return [i, checked[lookFor]]
            else:
                checked[n] = i
'''
Soln Explanation: pretty standard. values are the indices and num at each index is the key
'''