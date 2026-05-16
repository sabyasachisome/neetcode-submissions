class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for day_num, temp in enumerate(temperatures):
            while stack and stack[-1][0]<temp:
                i,j= stack.pop()
                res[j]= day_num-j
            stack.append((temp,day_num))
        return res