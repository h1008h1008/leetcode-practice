
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

## 📘 Types and Python Implementations

| Type              | Description                                       | Python Implementation       |
|-------------------|---------------------------------------------------|------------------------------|
| Truncate Toward 0 | Removes the decimal part, rounds **toward zero**  | `int(a / b)` ✅              |
| Floor Division     | Always rounds **down toward negative infinity**   | `a // b` ✅                  |

---

## 📌 Summary: Which to Use for What?

| Use Case                                | Recommended Syntax        | Notes                                   |
|-----------------------------------------|----------------------------|-----------------------------------------|
| Truncate toward zero (e.g. LeetCode)     | `int(a / b)`               | Common in integer division ✅            |
| Floor division (mathematical floor)     | `a // b`                   | Python’s default for `//`               |
| Ensure correct result with floats       | `int(float(a) / b)`        | Safely handles float division behavior  |

---

## 🧪 Code Examples

```python
print(int(7 / 2))       # 3
print(int(-7 / 2))      # -3  ✅ Truncate toward zero
print(-7 // 2)          # -4  ❌ Floor division (rounds down)
print(int(float(-7) / 2))  # -3 ✅ Consistent truncation

- You need to be really careful about mutable when update

```
## ✅ Muttable problem

You're right to worry about "modifying one cell affecting others" — that **can happen in Python**, but not in this case.

### ✅ Safe Case: Immutable Values

```python
counts = [0] * 26
counts[0] = 99
print(counts)
```

**Output:**

```python
[99, 0, 0, 0, ..., 0]  # Only index 0 is changed
```

This works correctly because `0` is an **immutable value**, and each index gets a **distinct integer object**.

---

### ❗ Dangerous Case: Shared References in 2D Lists

If you write:

```python
row = [[0] * 5] * 3
row[0][0] = 1
```

You’ll get:

```python
[[1, 0, 0, 0, 0],
 [1, 0, 0, 0, 0],
 [1, 0, 0, 0, 0]]  # ❌ All rows changed
```

This is because you copied **the same inner list reference** three times.

---

### ✅ Correct Way for 2D Lists

To get independent sublists:

```python
row = [[0] * 5 for _ in range(3)]
```

This creates a **new list for each row**, so modifying one doesn't affect the others.

