# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        len_a,len_b = 0,0
        p,q = headA,headB
        while(p):
            p = p.next
            len_a +=1
        while q:
            q = q.next
            len_b +=1
        p,q = headA,headB
        length = len_a - len_b if len_a > len_b else len_b - len_a
        if len_a >= len_b:
            i=1
            while i<=length:
                p = p.next
                i +=1
        else:
            i=1
            while i <= length:
                q = q.next
                i +=1
        while (p != q) and (p and q):
            p = p.next
            q = q.next
        return p
        
                