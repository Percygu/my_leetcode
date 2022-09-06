class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head,left: int, right: int):
        dummy = ListNode()
        dummy.next = head
        i, j = 0, 0
        p,q = dummy,dummy
        while i < left -1:
            p = p.next
            i += 1
        while j < right+1:
            q = p.next
            j += 1
        start, end= p,p.next
        pre,cur = p,p.next
        while cur != q:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        start.next = pre
        end.next = q
        return dummy.next










