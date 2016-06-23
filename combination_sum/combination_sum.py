# leetcode 39, combination sum, beats 15% submissions
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combination = []
        combinations = []
        self.dfs(candidates, target, combination, combinations)
        return combinations
    
    def dfs(self, candidates, target, combination, combinations):
        if target == 0:
            combinations.append(combination)
        if target < 0 or target == 0:
            return
        for num in candidates:
            if combination and num < combination[-1]:
                continue
            self.dfs(candidates, target - num, combination + [num], combinations)
            
            
# leetcode 39, combination sum, optimized version, beat 80% submission
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        combination = []
        combinations = []
        self.dfs(candidates, target, combination, combinations)
        return combinations
    
    def dfs(self, candidates, target, combination, combinations):
        if target == 0:
            combinations.append(combination)
            return
        for num in candidates:
            if num > target:
                break
            if combination and num < combination[-1]:
                continue
            self.dfs(candidates, target - num, combination + [num], combinations)
