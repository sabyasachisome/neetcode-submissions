from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_time(speed):
            time=0
            for pile in piles:
                time+=ceil(pile/speed)
            return time<=h
        
        left=1
        right= max(piles)
        while left<=right:
            mid= left+(right-left)//2
            if get_time(mid):
                right=mid-1
            else:
                left=mid+1
        return left

                
