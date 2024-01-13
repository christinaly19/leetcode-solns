# 219. Contains Duplicate II (EASY)

# A SLOW SOLUTION ATTEMPTING SLIDING WINDOW (DID NOT PASS TIME )
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # we will use a sliding window approach
        lIndex = 0
        while lIndex < len(nums):
            for i in range(1,k + 1):
                if lIndex + i >= len(nums):
                    break
                if nums[lIndex] == nums[lIndex+i]:
                    return True
            lIndex = lIndex + 1
        return False
            
        

            
        

# FAST SOLUTION USING HASH
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dictNums = {}
        for i, num in enumerate(nums):
            if num in dictNums and (i - dictNums[num] <= k):
                return True
            else:
                dictNums[num] = i
        return False

            
        