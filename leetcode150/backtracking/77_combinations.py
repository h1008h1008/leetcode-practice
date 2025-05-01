class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        path = []
        combinations = []
        options = list(range(1, n + 1))
        def backtrack(path,options):
            if len(path) == k:
                combinations.append(list(path))
                return
            for i in range(0,len(options)):
                path.append(options[i])
                backtrack(path,options[i+1:])
                path.pop()
        backtrack(path,options)
        return combinations
        