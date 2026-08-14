class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result= [0]*len(temperatures)
        # for idx in range(len(temperatures)):
        #     for idx2 in range(idx+1, len(temperatures)):
        #         if temperatures[idx2]>temperatures[idx]:
        #             result[idx]= idx2-idx
        #             break
        # return result

        # stack=[]
        # res=[0]*len(temperatures)
        # for day_num, temp in enumerate(temperatures):
        #     while stack and stack[-1][0]<temp:
        #         i,j= stack.pop()
        #         res[j]= day_num-j
        #     stack.append((temp,day_num))
        # return res
        stack=[]
        final_arr=[0]*len(temperatures)
        for cur_day, cur_temp in enumerate(temperatures):
            while stack and stack[-1][1]<cur_temp:
                prev_day,prev_temp= stack.pop()
                final_arr[prev_day]= cur_day-prev_day
            stack.append((cur_day,cur_temp))
        return final_arr
            

