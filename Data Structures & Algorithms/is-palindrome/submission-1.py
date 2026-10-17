class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reversed_lower_strn=""
        # normal_lower_strn=""
        # for char in s:
        #     if char.isalnum():
        #         reversed_lower_strn= char.lower()+ reversed_lower_strn
        #         normal_lower_strn+= char.lower()
        # return reversed_lower_strn==normal_lower_strn

        def check_alnum(char):
            return ord('a')<=ord(char)<=ord('z') or ord('A')<=ord(char)<=ord('Z') or ord('0')<=ord(char)<=ord('9')

        l, r= 0, len(s)-1
        while l<r:
            while l<r and not check_alnum(s[l]):
                l+=1
            while l<r and not check_alnum(s[r]):
                r-=1
            if s[l].lower()!= s[r].lower():
                return False
            l, r= l+1, r-1
        return True


