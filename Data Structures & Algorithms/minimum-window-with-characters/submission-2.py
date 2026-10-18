class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t= {}
        count_s= {}
        min_str=[-1,-1]
        min_val= float("inf")

        for char in t:
            # if char not in count_t:
            #     count_t[char]=1
            # else:
            #     count_t[char]+=1
            count_t[char]= 1+ count_t.get(char, 0)
        print(count_t)
        have, need= 0, len(count_t)
        
        left=0
        for right in range(len(s)):
            right_char= s[right]
            count_s[right_char]= 1+ count_s.get(right_char,0)

            if right_char in count_t and count_s[right_char]==count_t[right_char]:
                have+=1

            
            while have==need:
                if right-left+1<min_val:
                    min_val= right-left+1
                    min_str= [left, right]

                left_char= s[left]
                
                if left_char in count_t and count_s[left_char]==count_t[left_char]:
                    have-=1
                count_s[left_char]-=1
                left+=1
            
        return s[min_str[0]:min_str[1]+1]



