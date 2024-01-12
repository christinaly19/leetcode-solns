# 904. Fruit Into Baskets (Medium)


# FIRST ATTEMPT (BRUTE FORCED USING HASHMAPS)
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        maxFruits = 0
        for i, fruit in enumerate(fruits):
            fruitMap = {}
            fruitMap[fruit] = 1
            currSum = 1
            for j in range(i+1, len(fruits)):
                currSum = 0
                if fruits[j] in fruitMap:
                    fruitMap[fruits[j]] = fruitMap.get(fruits[j]) + 1
                else:
                    if len(fruitMap) >= 2:
                        currSum = sum(fruitMap.values())
                        break
                    else:
                        fruitMap[fruits[j]] = 1
                currSum = sum(fruitMap.values())
            if currSum > maxFruits:
                maxFruits = currSum
        return maxFruits

#SECOND ATTEMP (USES SLIDING WINDOW AND COUNTER)
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        maxFruits = 0
        r = 0
        l= 0 
        unique = 0
        fruit_types = Counter()
        while r < (len(fruits)):
            if fruit_types[fruits[r]] == 0:
                unique = unique + 1
                fruit_types[fruits[r]] = 1
            else:
                fruit_types[fruits[r]] = fruit_types[fruits[r]] + 1

            while unique >= 3:
                fruit_types[fruits[l]] = fruit_types[fruits[l]] - 1
                if fruit_types[fruits[l]] == 0:
                    # fruit is gone. no more
                    unique = unique - 1
                l = l + 1
            
            if (r - l + 1 > maxFruits):
                maxFruits = r - l + 1
            r = r + 1
            
        return maxFruits

'''
Had a rough time w this one...
'''