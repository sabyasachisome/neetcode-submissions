# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1= list1
        temp2= list2
        new_list= ListNode()
        head= new_list
        while list1 and list2:
            if list1.val<list2.val:
                val= list1.val
                list1=list1.next
            else:
                val= list2.val
                list2=list2.next
            tmp= ListNode(val)
            new_list.next= tmp
            new_list=new_list.next
        while list1:
            val= list1.val
            tmp= ListNode(val)
            new_list.next= tmp
            new_list=new_list.next
            list1=list1.next
        while list2:
            val= list2.val
            tmp= ListNode(val)
            new_list.next= tmp
            new_list=new_list.next
            list2=list2.next
        return head.next
        # while head:
        #     print(head.val)
        #     head=head.next
