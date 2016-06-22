#leetcode 1, two sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = {}
        for i in range(len(nums)):
            hashTable[nums[i]] = i
        
        for i in range(len(nums)):
            if target - nums[i] in hashTable and i != hashTable[target - nums[i]]:
                return [i, hashTable[target-nums[i]]]
        
        return []
