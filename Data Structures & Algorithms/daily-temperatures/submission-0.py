class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        final_res=[]
        
        for idx in range(len(temperatures)):
            greater_flag=0
            for idx2 in range(idx+1, len(temperatures)):
                if temperatures[idx]<temperatures[idx2]:
                    # final_res.append(idx2-idx)
                    greater_flag=1
                    break
            if greater_flag==1:
                # print(temperatures[idx],temperatures[idx2])
                final_res.append(idx2-idx)
            else:
                final_res.append(0)
        return final_res