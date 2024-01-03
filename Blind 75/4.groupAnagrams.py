# Problem 49
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        answ = []
        hashes = []
        for word in strs:
            compMap = {}
            # creating a hashmap that can be used for comparisons
            for letter in word:
                if letter in compMap:
                    compMap[letter] = compMap.get(letter) + 1
                else:
                    compMap[letter] = 1
            # seeing if hashmap exists, and adding to correct slot
            if compMap not in hashes:
                hashes.append(compMap)
                answ.append([word])
            else: 
                index = hashes.index(compMap)
                answ[index].append(word)
        return answ
    
'''
Much struggling to be had.
Created 2 arrays; one to store hashmaps for each unique anagram and another to store the answer; for each word, create a hashmap and then do comparisons with previous hashes to 
see if it is an exisitng anagram, and then push the string to the appropriate location in the answer array.
There is probably a better way to do this.
'''