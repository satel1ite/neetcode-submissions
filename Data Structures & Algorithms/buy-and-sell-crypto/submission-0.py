class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        cur = 0
        n = len(prices)
        buy = prices[0]
        for i in range(1, n):
            if prices[i] > buy:
                ans = max(ans, prices[i] - buy)
            else:
                buy = prices[i]
        return ans
