class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        ans = float('inf')
        arrsum = 0

        while fast < len(nums):
            arrsum += nums[fast]
            fast += 1

            while arrsum >= target:
                ans = min(ans, fast - slow)
                arrsum -= nums[slow]
                slow += 1

        return 0 if ans == float('inf') else ans

        