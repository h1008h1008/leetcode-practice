class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        map = {}
        while n != 1:
            if n in map:
                return False
            map[n] = 1
            num = 0
            for char in str(n):
                num += int(char)*int(char)
            n = num
        return True