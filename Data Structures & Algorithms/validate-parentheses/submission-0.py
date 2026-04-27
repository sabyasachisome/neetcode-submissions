class Solution:
    def isValid(self, s: str) -> bool:
        paran_map={')':'(','}':'{',']':'['}
        stack=[]
        for char in s:
            if stack and stack[-1]==paran_map.get(char):
                stack.pop()
            else:
                stack.append(char)
        return len(stack)==0