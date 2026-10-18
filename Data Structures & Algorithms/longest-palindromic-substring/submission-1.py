class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str= float("-inf")
        for idx in range(len(s)):
            left, right= idx, idx
            while left>=0 and right<len(s) and s[left]==s[right]:
                if right-left+1>=max_str:
                    max_str= right-left+1
                    max_start= left
                left-=1
                right+=1
            
            left, right= idx, idx+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                if right-left+1>=max_str:
                    max_str= right-left+1
                    max_start= left
                left-=1
                right+=1
        return s[max_start:max_start+max_str]