class Solution:
    def characterReplacement(self, s: str, k: int)-> int:
        # count = {}
        # res = 0

        # l = 0
        # max_freq = 0
        # for r in range(len(s)):
        #     count[s[r]]= 1+ count.get(s[r], 0)
        #     max_freq= max(max_freq, count[s[r]])
            
        #     while (r-l+1)- max_freq>k:
        #         count[s[l]]-=1
        #         l+=1
        #     res= max(res, r-l+1)
        # return res

        char_map={}
        left,right=0,0
        max_freq=0
        max_len=0
        while right<len(s):
            char_map[s[right]]= 1+char_map.get(s[right],0)
            max_freq= max(max_freq, char_map[s[right]])
            while (right-left+1)-max_freq>k:
                char_map[s[left]]-=1
                left+=1
            max_len= max(max_len,right-left+1)
            print(max_len)
            right+=1
        return max_len

            


