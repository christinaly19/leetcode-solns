# 575. Distribute Candies (Not part of  NeetCode, just for fun! )
class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        candiesMap = {}
        maxCanEat = len(candyType) / 2
        for candy in candyType:
            if candy in candiesMap:
                candiesMap[candy] = candiesMap.get(candy) + 1
            else:
                candiesMap[candy] = 1
        if len(candiesMap) <= maxCanEat:
            return len(candiesMap)
        else:
            return maxCanEat