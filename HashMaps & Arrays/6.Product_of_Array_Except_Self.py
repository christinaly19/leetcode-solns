#238. Product of Array Except Self
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        answ = [1] * n
        prefix[0] = 1
        #calculate prefix 
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        #calculate postfix
        postfix[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]
        #return value 
        for i in range(len(nums)):
            answ[i] = postfix[i] * prefix[i]
        return answ
'''
Prefix stores the product of all numbers before that number, while postfix stores the products after.
Had to look at hint for this one
'''