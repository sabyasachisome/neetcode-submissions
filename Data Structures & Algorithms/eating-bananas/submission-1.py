class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_time(k):
            total_time=0
            for pile in piles:
                time= math.ceil(float(pile)/k)
                total_time+=time
            return total_time
        
        l,r= 1, max(piles)
        res= max(piles)
        while l<=r:
            mid= l+(r-l)//2
            time_taken= get_time(mid)
            if time_taken<=h:
                res= mid
                r= mid-1
            else:
                l= mid+1
        return res


