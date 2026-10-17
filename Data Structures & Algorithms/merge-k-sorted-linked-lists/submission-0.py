# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        while len(lists)>1:
            mergedLists=[]
            for idx in range(0, len(lists), 2):
                l1= lists[idx]
                l2= lists[idx+1] if idx+1<len(lists) else None
                mergedLists.append(self.merge_list(l1, l2))
            lists= mergedLists
        return lists[0]
        
    def merge_list(self, l1, l2):
        tmp= dummy= ListNode()
        while l1 and l2:
            if l1.val<l2.val:
                tmp.next= l1
                l1= l1.next
            else:
                tmp.next= l2
                l2= l2.next
            tmp= tmp.next
        tmp.next= l1 if l1 else l2
        return dummy.next
            
