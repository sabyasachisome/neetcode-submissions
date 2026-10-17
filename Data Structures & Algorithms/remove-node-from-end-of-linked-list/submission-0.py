# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def get_length(start):
            tmp= start
            count=0
            while tmp:
                count+=1
                tmp= tmp.next
            return count
        ll_len= get_length(head)
        to_be_removed= ll_len-n+1

        print(to_be_removed)
        cur_ptr=0
        tmp= head
        
        if to_be_removed==1:
            return tmp.next

        while tmp:
            cur_ptr+=1
            if cur_ptr+1==to_be_removed:
                tmp.next= tmp.next.next
            tmp= tmp.next
        return head

        