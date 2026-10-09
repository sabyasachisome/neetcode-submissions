class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum= nums[0]
        res= max_sum

        for idx in range(1, len(nums)):
            max_sum= max(max_sum+ nums[idx], nums[idx])

            res= max(res, max_sum)
        
        return res