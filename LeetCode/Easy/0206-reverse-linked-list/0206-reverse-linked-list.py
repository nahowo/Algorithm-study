# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        nxt = head.next
        prv = None
        head.next = prv
        prv = head
        
        while nxt != None:
            head = nxt
            nxt = nxt.next
            head.next = prv
            prv = head
        return head