class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        if not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        numIslands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(i, j, m, n, grid)
                    numIslands += 1
        return numIslands
    
    def dfs(self, i, j, m, n, grid):
        if grid[i][j] == '1':
            grid[i][j] = '2'
            moves = [(1,0), (0,1), (-1,0), (0,-1)]
            for (movex, movey) in moves:
                def inBound(x, y, m, n):
                    return x >= 0 and x < m and y >= 0 and y < n
                    
                if inBound(i + movex, j + movey, m, n):
                    self.dfs(i + movex, j + movey, m, n, grid)
