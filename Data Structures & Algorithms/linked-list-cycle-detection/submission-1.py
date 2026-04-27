# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        seen= set()
        temp= head
        while temp:
            if temp in seen:
                return True
            seen.add(temp)
            temp=temp.next
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast= head, head
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
            if slow==fast:
                return True
        return False