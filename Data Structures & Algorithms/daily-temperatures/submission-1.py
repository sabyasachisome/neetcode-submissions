class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        final_res=[0]*len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t> stack[-1][0]:
                temp, ind= stack.pop()
                final_res[ind]=i-ind
            stack.append((t,i))
        return final_res