class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = float('inf')
        while left <= right:
            if nums[left] <= nums[right]:
                ans = min(ans, nums[left])
                break
            mid = (left + right) // 2
            ans = min(ans, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid - 1

        return ans