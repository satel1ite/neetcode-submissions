class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ar = set(nums)
        ans = 0
        res = 0
        for num in nums:
            if num - 1 not in ar:
                j = num
                res = 0
                while j in ar:
                    res += 1
                    j += 1
                ans = max(ans, res)
        return ans