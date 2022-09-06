class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int):
         return dfs(1,n)


    # dfs 返回以num为根节点的所有二叉树的根节点
    def dfs(self,l,r):
        res = []
        if l > r:
            res.append(None)
            return res
        for i in range(l,r+1):
            left = self.dfs(l,i-1)
            right = self.dfs(i+1,r)
            for lc in left:
                for rc in right:
                    root = TreeNode(i)
                    root.left,root.right = lc,rc
                    res.append(root)
        return res




