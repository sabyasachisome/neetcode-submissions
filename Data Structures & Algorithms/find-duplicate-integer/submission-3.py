class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for idx in range(len(nums)-1):
            if nums[idx]==nums[idx+1]:
                return nums[idx]