class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_map={}
        for elem in nums:
            hash_map[elem]= 1+hash_map.get(elem,0)
        for k,v in hash_map.items():
            if v>1:
                return k