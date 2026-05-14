class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis_map={"}":"{","]":"[",")":"("}
        stack=[]
        for char in s:
            if stack and paranthesis_map.get(char)==stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return len(stack)==0