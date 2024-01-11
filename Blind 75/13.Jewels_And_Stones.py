# 771. Jewels and Stones (Easy)
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        stoneMap = {}
        for stone in stones:
            if stone in stoneMap:
                stoneMap[stone] = stoneMap.get(stone) + 1
            else:
                stoneMap[stone] = 1
        count = 0
        for jewel in jewels:
            if jewel in stoneMap:
                count = count + stoneMap[jewel]
    
        return count