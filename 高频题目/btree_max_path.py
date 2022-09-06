# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global res
        res = -float('inf')
        def dfs(root):
            global res
            if not root:
                return 0
            left = max(0,dfs(root.left))
            right = max(0,dfs(root.right))
            res = max(res,root.val + left + right)   # 求当前节点的最大路径和
            return root.val + max(left,right)        # 

        dfs(root)
        return res

