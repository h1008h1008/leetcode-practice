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
    
# for any natural number n, regargless of the number of digits, the sum of the squares of its digits will always be 
# less than or equal to 81*len(str(n))^2. all number will converge in a finite set S
# by infinite loop the number will finally converge in S Repeatedly applying a function over a finite set must eventually result in a cycle;
    