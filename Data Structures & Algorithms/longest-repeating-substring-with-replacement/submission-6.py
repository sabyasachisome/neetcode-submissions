class Solution:
    # def characterReplacement(self, s: str, k: int) -> int:
    #     res=0
    #     for i in range(len(s)):
    #         freq_count, max_val={}, 0
    #         for j in range(i, len(s)):
    #             freq_count[s[j]]= 1+ freq_count.get(s[j],0)
    #             max_val= max(freq_count[s[j]], max_val)
    #             if (j-i+1)-max_val<=k:
    #                 res= max(res, (j-i+1))
    #     return res

    def characterReplacement(self, s: str, k: int)-> int:
        count = {}
        res = 0

        l = 0
        max_freq = 0
        for r in range(len(s)):
            count[s[r]]= 1+ count.get(s[r], 0)
            max_freq= max(max_freq, count[s[r]])
            
            while (r-l+1)- max_freq>k:
                count[s[l]]-=1
                l+=1
            res= max(res, r-l+1)
        return res
        count = {}
        res = 0

        # l = 0
        # maxf = 0
        # for r in range(len(s)):
        #     count[s[r]] = 1 + count.get(s[r], 0)
        #     maxf = max(maxf, count[s[r]])

        #     while (r - l + 1) - maxf > k:
        #         count[s[l]] -= 1
        #         l += 1
        #     res = max(res, r - l + 1)

        # return res