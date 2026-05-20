class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)==sorted(t)
    
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s)!=len(t):
    #         return False
    #     arr_s, arr_t=[0]*26,[0]*26
    #     for idx in range(len(s)):
    #         arr_s_idx= ord(s[idx])-ord('a')
    #         arr_s[arr_s_idx]+=1

    #         arr_t_idx= ord(t[idx])-ord('a')
    #         arr_t[arr_t_idx]+=1
    #     return arr_s==arr_t

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        count_arr=[0]*26
        for idx in range(len(s)):
            count_arr[ord(s[idx])-ord('a')]+=1
            count_arr[ord(t[idx])-ord('a')]-=1
        for ctr in count_arr:
            if ctr!=0:
                return False
        return True