
# DFS

```text
function DFS(i, j):
    if i or j is out of bounds OR grid[i][j] == 0:
        return 0

    mark grid[i][j] as visited

    for each direction (dx, dy) in [(0,1), (1,0), (-1,0), (0,-1)]:
        DFS(i + dx, j + dy)
```

# Binary Search Patterns: `[left, right)` vs `[left, right]`

Binary search is a fundamental algorithm used to find the position of a target value in a sorted array. There are two common interval notations used when implementing binary search.

---

## 📐 Interval Types

| Pattern           | Meaning                                | Loop Condition         | Final Return         |
|------------------|----------------------------------------|------------------------|----------------------|
| `[left, right)`  | Left-inclusive, right-exclusive         | `while left < right`   | Return `left`        |
| `[left, right]`  | Both ends inclusive                     | `while left <= right`  | Return `right + 1`   |

---

## 📘 Pattern 1: `[left, right)` — Right-exclusive

```python
class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return right
```
- Interval is [left, right)

- Stops when left == right

- right is never accessed directly (right is exclusive)

- Return value is right (or left, same value at the end)

## 📘 Pattern 2: [left, right] — Both-inclusive

```python
class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right + 1
```

- Interval is [left, right]

- Stops when left > right

- mid can reach all valid indices

- Return value is right + 1 (which equals left after the loop ends)


#  Common Rule of Thumb

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
