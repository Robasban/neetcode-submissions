# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.res = True

        def dfs(p, q):
            if (not p) and q:
                self.res = False
                return
            if p and (not q):
                self.res = False
                return
            if (not p) and (not q):
                return
            
            self.res = p.val == q.val and self.res

            dfs(p.left, q.left)
            dfs(p.right, q.right)

        dfs(p, q)

        return self.res            
