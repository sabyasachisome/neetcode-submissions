class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_lower_strn=""
        normal_lower_strn=""
        for char in s:
            if char.isalnum():
                reversed_lower_strn= char.lower()+ reversed_lower_strn
                normal_lower_strn+= char.lower()
        return reversed_lower_strn==normal_lower_strn