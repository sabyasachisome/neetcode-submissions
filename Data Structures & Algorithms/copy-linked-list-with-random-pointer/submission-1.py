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
        # copy_map={None: None}
        # temp= head
        # while temp:
        #     copy_map[temp]= Node(temp.val)
        #     temp= temp.next
        # temp= head
        # while temp:
        #     copy_map[temp].next= copy_map[temp.next]
        #     copy_map[temp].random= copy_map[temp.random]
        #     temp= temp.next
        # return copy_map[head]
        node_map, tmp= {None: None}, head
        while tmp:
            node_map[tmp]= Node(tmp.val)
            tmp= tmp.next
        tmp= head
        while tmp:
            print(tmp.val)
            cur_node= node_map[tmp]
            cur_node.next= node_map[tmp.next]
            cur_node.random= node_map[tmp.random]
            tmp= tmp.next
        return node_map[head]
