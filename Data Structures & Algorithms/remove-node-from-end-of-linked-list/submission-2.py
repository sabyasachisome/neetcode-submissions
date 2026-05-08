# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [1,2,3,4,5,6,7,8] n=2
# [1] n=1

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp= head
        count=0
        while tmp:
            tmp= tmp.next
            count+=1
        # print(count)
        del_ptr= count-n+1
        if del_ptr==1:
            return head.next
        # if count==1 and del_ptr==1:
        #     head= None
        #     return head
        # # print(del_ptr)
        tmp= head
        cur_ptr=0
        while tmp:
            cur_ptr+=1
            print(cur_ptr, del_ptr)
            if cur_ptr+1==del_ptr:
                tmp.next= tmp.next.next
                # print(tmp.val)
                break
            tmp= tmp.next
        return head


