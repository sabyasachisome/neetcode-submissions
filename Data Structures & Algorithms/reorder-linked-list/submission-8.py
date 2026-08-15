# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def find_midpoint(tmp):
            slow, fast= tmp, tmp.next
            while fast and fast.next:
                slow= slow.next
                fast= fast.next.next
                if slow==fast:
                    break
            return slow
        
        mid= find_midpoint(head)
        print(mid.val)
        
        def revert_ll(tmp):
            prev, cur= None, tmp
            while cur:
                tmp= cur.next
                cur.next= prev
                prev= cur
                cur= tmp
            return prev
        reverted_head= revert_ll(mid.next)
        mid.next= None
        # print(reverted_head.val)
        l1, l2= head, reverted_head
        # print(l1.val)
        # print(l2.val)
        while l1 and l2:
            tmp1, tmp2= l1.next, l2.next
            l1.next= l2
            l2.next= tmp1
            l1, l2= tmp1, tmp2


