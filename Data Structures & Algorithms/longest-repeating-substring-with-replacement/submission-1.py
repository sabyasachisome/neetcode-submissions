class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map={}
        left, right= 0,0
        max_freq= float("-inf")
        res= float("-inf")
        while right<len(s):
            freq_map[s[right]]= 1+ freq_map.get(s[right],0)
            max_freq= max(max_freq, freq_map[s[right]])
            while (right-left+1)-max_freq>k:
                freq_map[s[left]]-=1
                left+=1
            res= max(res, right-left+1)
            right+=1
        return res