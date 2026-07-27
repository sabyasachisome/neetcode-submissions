class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # points.sort(key= lambda x: x[0]**2 + x[1]**2)
        # return points[:k]
        min_heap=[]
        final_res=[]
        for x,y in points:
            min_heap.append((x**2+y**2,x,y))
        print(min_heap)
        heapq.heapify(min_heap)
        print(min_heap)
        while k>0:
            closest= heapq.heappop(min_heap)
            final_res.append([closest[1],closest[2]])
            k-=1
        return final_res