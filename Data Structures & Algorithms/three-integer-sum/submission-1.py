class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                if (nums[left] + nums[right] == -nums[i]):
                    ans.append([nums[left], nums[right], nums[i]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif (nums[left] + nums[right] > -nums[i]):
                    right -= 1
                elif (nums[left] + nums[right] < -nums[i]):
                    left += 1
        return ans