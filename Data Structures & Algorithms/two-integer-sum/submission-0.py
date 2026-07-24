class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = dict()
        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in dct:
                return [dct[diff], i]
            dct[num] = i
