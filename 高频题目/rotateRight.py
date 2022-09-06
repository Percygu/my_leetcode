'''
旋转链表
lc:61
思路：从链表的倒数第k个结点开始，把后面的节点移动到链表的前面
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # 找到倒数第k+1个节点
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n += 1

        dummy = ListNode()
        dummy.next = head
        p = dummy
        k %= n
        while k:
            p = p.next
            k -= 1

        slow = dummy
        fast = p
        while fast.next:
            slow = slow.next
            fast = fast.next

        # 此时slow走到倒数第k+1个节点,fast走到最后一个节点
        # 断开重连
        fast.next = head
        new = slow.next
        slow.next = None
        return new








