class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def backtrack(path,left,right):
            if len(path) == n*2:
                result.append(path)
                return
            if left < n:
                backtrack(path + "(",left+1,right)
            if left > right:
                backtrack(path + ")",left,right+1)
            
        backtrack("",0,0)
        return result
        