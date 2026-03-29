# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node, p, q):

            if node.val < p.val and node.val < q.val:
                return dfs(node.right, p, q)

            if node.val > p.val and node.val > q.val:
                return dfs(node.left, p, q)

            return node

        return dfs(root, p, q)

        



    #     5
    #    / \
    #   3     8
    #  / \   / \
    # 1   4 7   9
    #  \
    #   2