# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return None
        elif list1==None:
            return list2
        elif list2==None:
            return list1
        
        if list1.val<=list2.val:
            head=list1
            list1=list1.next
        else:
            head=list2
            list2=list2.next
        first=head
        
        while True:    
            if list1==None:
                head.next=list2
                break
            elif list2==None:
                head.next=list1
                break
                
            if list1.val<=list2.val:
                head.next=list1
                head=head.next
                list1=list1.next
            else:
                head.next=list2
                head=head.next
                list2=list2.next
                
        return first