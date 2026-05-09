class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen_set= set()
        for num in nums:
            if num in seen_set:
                return num
            seen_set.add(num)