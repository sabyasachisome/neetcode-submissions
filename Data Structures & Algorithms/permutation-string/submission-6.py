class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_arr, s2_arr= [0]*26, [0]*26
        if len(s1)>len(s2):
            return False
        matches=0
        for idx in range(len(s1)):
            s1_arr[ord(s1[idx])- ord('a')]+=1
            s2_arr[ord(s2[idx])- ord('a')]+=1
        print(s1_arr)
        print(s2_arr)
        for idx in range(26):
            if s1_arr[idx]==s2_arr[idx]:
                matches+=1
        print(matches)
        if matches==26:
            return True
        l=0
        for r in range(len(s1), len(s2)):
            if matches==26:
                return True
            idx= ord(s2[r])- ord('a')
            s2_arr[idx]+=1

            if s1_arr[idx]+1==s2_arr[idx]:
                matches-=1
            elif s1_arr[idx]==s2_arr[idx]:
                matches+=1
                 
            idx= ord(s2[l])- ord('a')
            s2_arr[idx]-=1
            if s1_arr[idx]-1==s2_arr[idx]:
                matches-=1
            elif s1_arr[idx]==s2_arr[idx]:
                matches+=1
            l+=1

        return matches==26
