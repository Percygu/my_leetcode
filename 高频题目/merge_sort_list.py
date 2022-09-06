# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if not head:
            return None
        return self.sort(head)


    def sort(self,head):
        # 只有一个节点，直接返回
        if not head.next:
            return head
        slow,fast = head,head.next
        while fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        h1 = self.sort(head)
        h2 = self.sort(second)
        h = self.merge(h1,h2)
        return h



    # 合并两个有序链表
    def merge(self,h1,h2):
        if not h1:
            return h2
        if not h2:
            return h1
        if h1.val < h2.val:
            h1.next = self.merge(h1.next,h2)
            return h1
        else:
            h2.next = self.merge(h1,h2.next)
            return h2