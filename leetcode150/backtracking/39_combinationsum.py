class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(list(path))
                return
            elif total > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # not i + 1 because we can reuse same element
                path.pop()

        backtrack(0, [], 0)
        return result
