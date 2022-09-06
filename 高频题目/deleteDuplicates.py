# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 通过遍历找到每个相同重复值的最后一个重复节点
        if not head or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        pre,cur = dummy,dummy.next
        while cur:
            while cur and cur.next and cur.val == cur.next.val:
                cur = cur.next
            # 没有重复节点
            if pre.next == cur:
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return dummy.next


