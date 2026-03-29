# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.tree1, self.tree2 = [], []

        def dfs(node, tree):

            if not node:
                tree.append(None)
                return

            tree.append(node.val)

            dfs(node.left, tree)
            dfs(node.right, tree)
            return tree

        print(self.tree1, self.tree2)

        return dfs(p, self.tree1) == dfs(q, self.tree2)
