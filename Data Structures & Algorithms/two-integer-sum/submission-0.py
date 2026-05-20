class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_pair={}
        for idx in range(len(nums)):
            if target-nums[idx] in target_pair:
                return ([target_pair[target-nums[idx]],idx])
            target_pair[nums[idx]]=idx
