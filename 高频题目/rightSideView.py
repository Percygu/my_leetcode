'''
二叉树的右视图
lc:199
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        res = []
        deepth = [0]
        def dfs(root,deep):
            if not root:
                return
            deep += 1
            # 只记录第一次到达该层的点，按照 中-右-左遍历 一定是右视图
            print(root.val,deep,deepth)
            if deep > deepth[-1]:
                deepth.append(deep)
                res.append(root.val)
            dfs(root.right,deep)
            dfs(root.left,deep)
        dfs(root,0)
        return res


