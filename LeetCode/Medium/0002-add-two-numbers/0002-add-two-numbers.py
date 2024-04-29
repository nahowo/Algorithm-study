# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=[]
        s2=[]
        while l1!=None:
            s1.append(l1.val)
            l1=l1.next
        while l2!=None:
            s2.append(l2.val)
            l2=l2.next
        
        n1=len(s1)
        n2=len(s2)
        if n1>n2:
            s2+=[0]*(n1-n2+1)
            s1+=[0]
        else:
            s1+=[0]*(n2-n1+1)
            s2+=[0]
        
        s=deque([0]*len(s1))
        for i in range(len(s1)-1):
            s[i]+=(s1[i]+s2[i])%10
            s1[i+1]+=(s1[i]+s2[i])//10
        s[-1]+=s1[-1]
        if s[-1]==0:
            s.pop()
        
        x=s.popleft()
        answer=ListNode(x,None)
        head=answer
        for i in range(len(s)):
            x=s.popleft()
            answer.next=ListNode(x,None)
            answer=answer.next
        return head