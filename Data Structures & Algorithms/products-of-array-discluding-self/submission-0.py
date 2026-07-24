class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix = [1] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = nums[i] * prefix[i - 1]
            
        suffix = [1] * n
        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1] 
            
        ans = [1] * n
        for i in range(n):
            left_prod = prefix[i - 1] if i > 0 else 1
            right_prod = suffix[i + 1] if i < n - 1 else 1
            
            ans[i] = left_prod * right_prod
            
        return ans
