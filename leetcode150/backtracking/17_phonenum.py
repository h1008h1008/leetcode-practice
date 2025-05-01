class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        n = len(digits)
        def backtrack(path, i):
            if len(path) == n:
                ans = str(path)
                if path != "":
                    result.append(ans)
                return
            for letter in digit_to_letters[digits[i]]:
                backtrack(path + letter,i+1)
        backtrack("",0)
        return result