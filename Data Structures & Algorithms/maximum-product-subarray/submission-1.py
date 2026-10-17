class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # min_val, max_val= 1, 1
        max_val, min_val=1, 1
        res= float("-inf")
        for num in nums:
            temp= max_val*num
            max_val= max(max_val*num, min_val*num, num)
            min_val= min(temp, min_val*num, num)
            res= max(max_val, res)
        return res