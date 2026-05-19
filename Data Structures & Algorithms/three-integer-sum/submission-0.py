class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet=[]
        nums.sort()
        for first in range(len(nums)):
            
            if first>0 and nums[first]==nums[first-1]:
                continue

            triplet_sum=0
            second, third= first+1, len(nums)-1
            
            while second<third:
                triplet_sum= nums[first]+nums[second]+nums[third]
                if triplet_sum<0:
                    second+=1
                elif triplet_sum>0:
                    third-=1
                else:
                    triplet.append([nums[first],nums[second],nums[third]])
                    second+=1
                    third-=1
                    while nums[second]==nums[second-1] and second<third:
                        second+=1
        return triplet
