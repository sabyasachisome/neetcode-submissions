class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-1*stone for stone in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            heaviest= -1*heapq.heappop(stones)
            second_heaviest= -1*heapq.heappop(stones)
            if heaviest>second_heaviest:
                heapq.heappush(stones, -1*(heaviest-second_heaviest))
        
        stones.append(0)

        return -1*stones[0]