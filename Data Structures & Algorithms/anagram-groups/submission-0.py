class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strn_dict={}
        final_list=[]
        for strn in strs:
            strn_arr= [0]*26
            for char in strn:
                strn_arr[ord(char)-ord('a')]+=1
            if tuple(strn_arr) not in strn_dict:
                strn_dict[tuple(strn_arr)]= [strn]
            else:
                strn_dict[tuple(strn_arr)].append(strn)
        for k,v in strn_dict.items():
            # print(v)
            final_list.append(v)
        return final_list