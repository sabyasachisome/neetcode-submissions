class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed_pair=[(p,s) for p,s in zip(position,speed)]
        
        pos_speed_pair.sort(reverse=True)
        stack=[]
        for p,s in pos_speed_pair:
            time_taken= (target-p)/s
            stack.append(time_taken)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)