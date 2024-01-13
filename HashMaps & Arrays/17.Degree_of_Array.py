
# 697. Degree of an Array (Easy)
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find the degree 
        numbers = Counter(nums)
        degree = max(numbers.values())
        possibleNums = []
        for num in numbers:
            if numbers[num] == degree:
                possibleNums.append(num)
        print(possibleNums)
        
        # get initial value for lowest
        startingIndex = nums.index(possibleNums[0])
        currLength = 0
        currDegree = 0
        for i in range(startingIndex, len(nums)):
            currLength = currLength + 1
            if (nums[i] == possibleNums[0]):
                currDegree = currDegree + 1
            if currDegree == degree:
                break
        lowestSoFar = currLength 
        # if there are more values to check
        if len(possibleNums) > 1:
            for toCheck in possibleNums[1:]:
                startingIndex = nums.index(toCheck)
                currLength = 0
                currDegree = 0
                for i in range(startingIndex, len(nums)):
                    currLength = currLength + 1
                    if (nums[i] == toCheck):
                        currDegree = currDegree + 1
                    if currDegree == degree:
                        break
                if currLength < lowestSoFar:
                    lowestSoFar = currLength
        return lowestSoFar

'''
This one went ok. probably redundant code though
'''

