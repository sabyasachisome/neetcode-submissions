class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            idx= abs(num)-1
            if nums[idx]<0:
                return abs(num)
            nums[idx]*=-1
        # return -1

        # nums = [1,2,3,2,2]
        # nums = [1,4,2,3,2]
        # slow=1
        # fast= 