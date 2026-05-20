class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)==sorted(t)
        if len(s)!=len(t):
            return False
        arr_s, arr_t=[0]*26,[0]*26
        for idx in range(len(s)):
            arr_s_idx= ord(s[idx])-ord('a')
            arr_s[arr_s_idx]+=1

            arr_t_idx= ord(t[idx])-ord('a')
            arr_t[arr_t_idx]+=1
        return arr_s==arr_t