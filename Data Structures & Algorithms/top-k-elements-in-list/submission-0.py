class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map={}
        freq_bucket=[[] for _ in range(len(nums)+1)]
        final_res=[]
        for idx, num in enumerate(nums):
            freq_map[num]= 1+freq_map.get(num,0)
        
        for num,freq in freq_map.items():
            freq_bucket[freq].append(num)
        
        for i in range(len(freq_bucket)-1,-1,-1):
            if freq_bucket[i]:
                for elem in freq_bucket[i]:
                    final_res.append(elem)
            if len(final_res)==k:
                return final_res