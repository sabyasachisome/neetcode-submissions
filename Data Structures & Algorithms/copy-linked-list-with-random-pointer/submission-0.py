"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_map={None: None}
        temp= head
        while temp:
            copy_map[temp]= Node(temp.val)
            temp= temp.next
        temp= head
        while temp:
            copy_map[temp].next= copy_map[temp.next]
            copy_map[temp].random= copy_map[temp.random]
            temp= temp.next
        return copy_map[head]
