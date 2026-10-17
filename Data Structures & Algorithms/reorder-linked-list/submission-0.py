# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def get_midpoint(node):
            slow, fast= node, node.next
            while fast and fast.next:
                slow= slow.next
                fast= fast.next.next
            return slow
        
        mid_node= get_midpoint(head)
        print(mid_node.val)

        def revert_linkedlist(node):
            cur, prev= node, None
            while cur:
                next_node= cur.next
                cur.next= prev
                prev= cur
                cur= next_node
            return prev
        reverted_head= revert_linkedlist(mid_node)
        print(reverted_head.val)
        # 2->4
        # 8->6
        mid_node.next= None

        l1, l2= head, reverted_head
        while l1 and l2:
            tmp1= l1.next
            tmp2= l2.next
            l1.next= l2
            l2.next= tmp1
            l1, l2= tmp1, tmp2

            

