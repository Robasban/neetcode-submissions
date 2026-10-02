# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        self.res = None
        
        def dfs(root):
            if not root:
                return 

            if p.val < q.val and not self.res:
                if p.val <= root.val and root.val <= q.val:
                    self.res = root
            elif q.val <= p.val and not self.res:
                if q.val <= root.val and root.val <= p.val:
                    self.res = root

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return self.res
            