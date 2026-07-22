class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow, fast= 0,0
        # while True:
        #     slow= nums[slow]
        #     fast= nums[nums[fast]]
        #     if slow==fast:
        #         break

        # slow2=0
        # while True:
        #     slow= nums[slow]
        #     slow2= nums[slow2]
        #     if slow==slow2:
        #         return slow
        for ind,num in enumerate(nums):
            idx= abs(num)-1
            if nums[idx]<0:
                return abs(nums[ind])
            nums[idx]*=-1
            
