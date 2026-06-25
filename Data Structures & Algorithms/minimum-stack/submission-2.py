class MinStack:

    def __init__(self):
        self.minstack=[]

    def push(self, val: int) -> None:
        self.minstack.append(val)

    def pop(self) -> None:
        self.minstack.pop()
        

    def top(self) -> int:
        return self.minstack[-1]
        

    def getMin(self) -> int:
        min_val= float("inf")
        for idx in range(len(self.minstack)):
            min_val= min(min_val, self.minstack[idx])
        # tmp=[]
        # min_val= self.minstack[-1]
        # while self.minstack:
        #     val= self.minstack.pop()
        #     min_val= min(min_val,val)
        #     tmp.append(val)
        # while tmp:
        #     self.minstack.append(tmp.pop())
        return min_val
