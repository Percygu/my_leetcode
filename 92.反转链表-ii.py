#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre = None
        current = head
        while current:
            stamp = current.next
            current.next = pre
            pre = current          #pre 和 current 同时后移一个单位
            current = stamp
        return pre

            
        
# @lc code=end

'''
在遍历是，当前节点要指向前一节点，所以指向了前一节点后，就到不了后一节点了，要用一个暂存节点存下其后一个节点的值
'''