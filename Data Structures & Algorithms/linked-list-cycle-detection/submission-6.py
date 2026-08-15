# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow, fast= head, head
        # while fast and fast.next:
        #     slow= slow.next
        #     fast= fast.next.next
        #     if slow==fast:
        #         return True
        # return False
        seen_set= set()
        temp= head
        while temp:
            temp= temp.next
            if temp in seen_set:
                return True
            seen_set.add(temp)
        return False

