class Solution:
    # def findMin(self, nums: List[int]) -> int:
        # left, right= 0, len(nums)-1
        # res= nums[0]
        # while left<=right:
        #     if nums[left]<nums[right]:
        #         res= min(res, nums[left])
        #         break
        #     mid= left+ (right-left)//2
        #     res= min(nums[mid],res)
        #     if nums[mid]>=nums[left]:
        #         left=mid+1
        #     else:
        #         right=mid-1
        # return res
    
    def findMin(self, nums: List[int]) -> int:
        # left, right=0,len(nums)-1
        # if nums[left]<=nums[right]:
        #     return nums[left]
        # while left<right:
        #     mid= left+(right-left)//2
        #     if nums[mid]>nums[right]:
        #         left=mid+1
        #     else:
        #         right=mid
        
        # return (nums[mid+1] if len(nums)%2==0 else nums[mid])
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        return nums[pivot]
        # l, r = 0, len(nums) - 1
