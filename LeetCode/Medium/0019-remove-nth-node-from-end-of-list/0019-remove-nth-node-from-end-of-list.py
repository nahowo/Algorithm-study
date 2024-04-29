# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt=0
        pointer=head
        while pointer!=None:
            pointer=pointer.next
            cnt+=1
        if cnt==1:
            head=None
            return head
        num=cnt-n
        if cnt==n:
            head=head.next
            return head
        
        pointer=head
        for i in range(num-1):
            head=head.next
        if n==1:
            head.next=None
        else:
            head.next=head.next.next
        head=pointer
        return head