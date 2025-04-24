# leetcode-practice

## DFS

```text
function DFS(i, j):
    if i or j is out of bounds OR grid[i][j] == 0:
        return 0

    mark grid[i][j] as visited

    for each direction (dx, dy) in [(0,1), (1,0), (-1,0), (0,-1)]:
        DFS(i + dx, j + dy)
```
