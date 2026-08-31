# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p < root and q > root or p > root and q < root:
        #   root is LCA
        # if p < root and q < root:
        #   recursive down the left tree
        # if p > root and q > root:
        #   recursive down the right tree
        if (p.val <= root.val and q.val >= root.val) or (p.val >= root.val and q.val <= root.val):
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)