class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        deep,res = [],[]
        global deepth

        def dfs(self, root):
            if not root:
                return
            deepth += 1
            print(deepth,deep[-1])
            if (deepth > deep[-1]):
                deep.append(deepth)
                res.append(root.val)
            dfs(root.right)
            dfs(root.left)
        return dfs(root,0)