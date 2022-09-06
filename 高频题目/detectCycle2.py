'''
环形链表2
'''
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow,fast = head,head
        while True:
            if fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    break
                else:
                    return None

        fast = head
        while fast and fast != head:
            fast = fast.next
            slow = slow
        return fast

