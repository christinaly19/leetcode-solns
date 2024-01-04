# Question 217. Contains Duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prevMap = {}
        for i, n in enumerate(nums):
            if n in prevMap and prevMap[n] == 1:
                return True
            prevMap[n] = prevMap.get(n, 0) + 1
        return False


'''
Solution Explanation: 
- This uses a hashmap, O(n) time. 
- Iterates through nums and checks if n (key) is in the Hashmap. If it is, and occurrence is already 1, return true 
- Otherwise, it adds 1 to the default value of n 
'''