class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_set= set()
        left, right=0,0
        max_seq= 0
        for right in range(len(s)):
            while s[right] in seen_set:
                seen_set.remove(s[left])
                left+=1
            max_seq= max(max_seq, right-left+1)
            seen_set.add(s[right])
        return max_seq