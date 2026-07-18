class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_set= set()
        l,r=0,0
        max_len= 0
        for r in range(len(s)):
            while s[r] in seen_set:
                seen_set.remove(s[l])
                l+=1
            seen_set.add(s[r])
            max_len= max(max_len, r-l+1)
        return max_len
