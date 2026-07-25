class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        ans = 0
        n = len(height)
        r = n - 1
        max_l = height[l]
        max_r = height[r]
        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                ans += max_l - height[l]
            elif max_l >= max_r:
                r -= 1
                max_r = max(max_r, height[r])
                ans += max_r - height[r]
        return ans