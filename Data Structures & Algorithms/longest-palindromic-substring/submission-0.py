class Solution:
    def longestPalindrome(self, s: str) -> str:
        start_idx=0
        sub_len=0
        for idx in range(len(s)):
            l,r= idx, idx
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>sub_len:
                    start_idx=l
                    sub_len= r-l+1
                l-=1
                r+=1
            
            l,r= idx, idx+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>sub_len:
                    start_idx=l
                    sub_len= r-l+1
                l-=1
                r+=1
        return s[start_idx:start_idx+sub_len]
