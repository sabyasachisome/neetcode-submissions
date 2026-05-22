class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     final_arr=[]
    #     for idx in range(len(nums)):
    #         total_prod=1
    #         for idx2 in range(len(nums)):
    #             if idx==idx2:
    #                 continue
    #             total_prod*=nums[idx2]
    #         final_arr.append(total_prod)
    #     print(final_arr)
    #     return final_arr
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix= 1
        res=[1]*len(nums)
        for idx in range(len(nums)):
            res[idx]*=prefix
            prefix*= nums[idx]
        
        postfix=1
        for idx in range(len(nums)-1,-1,-1):
            res[idx]*=postfix
            postfix*=nums[idx]
        
        return res


