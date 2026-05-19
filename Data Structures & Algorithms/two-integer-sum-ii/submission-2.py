class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right=0, len(numbers)-1
        all_pairs=[]
        while left<right:
            tot_sum= numbers[left]+numbers[right]
            if tot_sum<target:
                left+=1
            elif tot_sum>target:
                right-=1
            else:
                all_pairs.append([left+1,right+1])
                left+=1
                right-=1
                while numbers[left]==numbers[left-1] and left<right:
                    left+=1
        print(all_pairs)
        return all_pairs[0]