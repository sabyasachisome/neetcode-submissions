class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        count_t= {}
        count_s= {}
        for char in t:
            count_t[char]= 1+count_t.get(char,0)
        # print(count_t)

        dist_need= len(count_t)
        dist_have= 0

        left=0
        res, res_len= [-1,-1], float("inf")
        for right in range(len(s)):
            right_char= s[right]
            count_s[right_char]= 1+ count_s.get(right_char,0)
        # print(count_s)

            if right_char in count_t and count_s[right_char]==count_t[right_char]:
                dist_have+=1
            
            while dist_have==dist_need:
                if right-left+1<=res_len:
                    res_len= min(res_len, right-left+1)
                    res=[left, right]
                
                left_char= s[left]
                if left_char in count_t and count_s[left_char]==count_t[left_char]:
                    dist_have-=1
                left+=1
                count_s[left_char]-=1
        return s[res[0]:res[1]+1]




