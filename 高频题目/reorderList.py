'''
重排链表
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or head.next:
            return head
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 第一个链表的最后一个节点为slow
        second = slow.next
        slow .next = None
        self.reverseList(second)

        self.linkList(head,second)
        return head




    def reverseList(self,head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


    def linkList(self,first,second):
        p1,p2 = first,second
        while p2:
            tmp = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p1.next
            p2 = tmp
        return first






