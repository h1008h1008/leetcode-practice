from collections import deque
class Solution(object):
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        count = 0
        def bfs(i,j):
            queue = deque()
            queue.append((i,j))
            while queue:
                (i,j) = queue.popleft()
                for dx , dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                    if m > i + dx >= 0 and n > j + dy >= 0 and grid[i+dx][j+dy] == "1":
                        queue.append((i+dx,j+dy))
                        grid[i+dx][j+dy] = "0"

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i, j)
        return count

        