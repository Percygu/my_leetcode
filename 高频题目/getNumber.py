'''
二叉树染色
LCP:52
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxValue(self, root: TreeNode, k: int) -> int:

        def dfs(root):
            dp = [0 for _ in range(k+1)]   # 表示包含当前根节点的子树中，与根节点相连的这一些节点，共有i个蓝色节点的最大和
            if not root:
                return dp
            left = dfs(root.left)
            right = dfs(root.right)

            dp[0] = max(left) + max(right)
            for i in range(1,k+1):
                for j in range(i):
                    dp[i] = max(dp[i],root.val + left[j] + right[k-j-1])
            return dp

        return max(dfs(root))