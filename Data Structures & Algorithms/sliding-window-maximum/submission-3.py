class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        n = len(nums)
        ans = []
        maxi = 0
        cur = 0
        if k == 1:
            return nums
        for right in range(k-1, n):
            cur = max(nums[left:right+1])
            
            ans.append(cur)
            left += 1
        return ans
