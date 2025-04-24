class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        m , n = len(grid) , len(grid[0])
        area = 1
        maxarea = 0
        def dfs(i,j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1
            for (dx,dy) in directions:
                area += dfs(i+dx,j+dy)
            return area
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    maxarea = max(maxarea,area)
        return maxarea
            
        