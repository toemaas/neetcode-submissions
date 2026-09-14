# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not p or not q:
            return None
        def dfs(node, p, q):
            if not node:
                return None
            
            if p <= node.val and node.val <= q:
                return node
            
            return dfs(node.left, p, q) or dfs(node.right, p, q)
        
        return dfs(root, min(p.val, q.val), max(p.val, q.val))
