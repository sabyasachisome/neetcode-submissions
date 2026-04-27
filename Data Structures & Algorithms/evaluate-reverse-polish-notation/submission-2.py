class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for char in tokens:
            if char not in "+-/*":
                stack.append(char)
            else:
                num1= int(stack.pop())
                num2= int(stack.pop())
                if char=='+':
                    res= num1+num2
                elif char=='-':
                    res= num2-num1
                elif char=='*':
                    res= num1*num2
                else:
                    res= num2/num1
                stack.append(res)
        return int(stack[-1])