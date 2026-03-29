# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.tree = []

        def dfs(node, tree):

            if not node:
                return

            if node.left:
                dfs(node.left, tree)

            tree.append(node.val)

            if node.right:
                dfs(node.right, tree)


        dfs(root, self.tree)

        return self.tree[k-1]