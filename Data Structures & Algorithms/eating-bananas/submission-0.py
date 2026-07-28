from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = float('inf')
        while left <= right:
            mid = (left + right) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
            if time <= h:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans