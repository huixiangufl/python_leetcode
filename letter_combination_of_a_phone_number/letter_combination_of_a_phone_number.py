class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.mapping = {'0' : '', '1' : '', '2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz' }
        combinations = []
        self.dfs(digits, 0, '', combinations)
        return combinations
    
    def dfs(self, digits, pos, combination, combinations):
        if pos == len(digits):
            if combination:
                combinations.append(combination)
            return
        for c in self.mapping[digits[pos]]:
            self.dfs(digits, pos + 1, combination + c, combinations)
