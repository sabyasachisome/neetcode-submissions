class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_map={}
        final_res=[]
        for strn in strs:
            arr= [0]*26
            for char in strn:
                arr[ord(char)-ord('a')]+=1
            print(arr)
            if tuple(arr) not in all_map:
                all_map[tuple(arr)]=[strn]
            else:
                all_map[tuple(arr)].append(strn)
        for k,v in all_map.items():
            final_res.append(v)
        return final_res