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

##  Common Rule of Thumb

| Type        | Mutable? | Example                  |
|-------------|----------|--------------------------|
| `list`      | ✅ Yes   | `[1, 2, 3]`              |
| `dict`      | ✅ Yes   | `{"a": 1, "b": 2}`       |
| `set`       | ✅ Yes   | `{1, 2, 3}`              |
| `str`       | ❌ No    | `"hello"`                |
| `tuple`     | ❌ No    | `(1, 2, 3)`              |
| `int`       | ❌ No    | `5`                      |
| `float`     | ❌ No    | `3.14`                   |
| `bool`      | ❌ No    | `True`                   |
| `frozenset` | ❌ No    | `frozenset([1, 2, 3])`   |

## 💡 Tips

- **Mutable** objects can be changed in place without creating a new object.
- **Immutable** objects require re-assignment if you want to change their value.
- You need to be really careful about mutable when update answers 
