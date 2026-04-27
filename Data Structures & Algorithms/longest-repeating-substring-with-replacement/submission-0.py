class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        for i in range(len(s)):
            freq_count, max_val={}, 0
            for j in range(i, len(s)):
                freq_count[s[j]]= 1+ freq_count.get(s[j],0)
                max_val= max(freq_count[s[j]], max_val)
                if (j-i+1)-max_val<=k:
                    res= max(res, (j-i+1))
        return res