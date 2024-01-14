# 2379. Minimum Recolors to Get K Consecutive Black Blocks (Easy)
class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        currK = 0
        arr = []
        # lets find a starting point for min changes
        while currK != k :
            arr.append(blocks[currK])
            currK = currK + 1
        bwCount = Counter(arr)
        minChanges = bwCount['W']
        while currK < len(blocks):
            toRemove = currK - k
            if blocks[toRemove] == 'W':
                bwCount['W'] = bwCount['W'] - 1
            else:
                bwCount['B'] = bwCount['B'] - 1
            if blocks[currK] == 'B':
                bwCount['B'] = bwCount['B'] + 1
            else:  
                bwCount['W'] = bwCount['W'] + 1
            currChanges = bwCount['W']
            minChanges = min(currChanges, minChanges)
            currK = currK + 1
        return minChanges
'''
Needed to be careful about the indexing for currK and K
Simple sliding window that removes the previous index B/W, and then adds the next one 
'''