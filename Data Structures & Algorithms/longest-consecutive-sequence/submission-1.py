class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen_set=set(nums)
        max_len=0
        for idx, elem in enumerate(nums):
            count=1
            if elem-1 not in seen_set:
                while elem+count in seen_set:
                    count+=1
            
            max_len= max(max_len, count)
        return max_len

