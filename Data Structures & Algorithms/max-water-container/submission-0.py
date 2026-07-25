class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        cur = 0
        best = 0
        n = len(heights)
        r = n - 1
        while l < r:
            cur = (r - l) * min(heights[l], heights[r])
            best = max(best, cur)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        return best