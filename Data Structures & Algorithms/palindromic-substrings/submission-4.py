class Solution:
    def countSubstrings(self, s: str) -> int:
        all_subs=0
        for idx in range(len(s)):
            left, right= idx, idx
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                all_subs+=1
                # print(s[left])
            left, right= idx, idx+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                all_subs+=1
                left-=1
                right+=1
                
        return all_subs
