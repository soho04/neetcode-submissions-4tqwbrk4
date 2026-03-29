# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.maxDia = 0

        def dfs(node):

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.maxDia = max(self.maxDia, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.maxDia
            
        
        # 1, null, 2, 3, 4, 5

        # [2, 3, 4]

            
        # 1, null, 2, 3, 4, null, 5, null, 6

        #           1
        #            \
        #             2
        #            / \
        #           3   4
        #            \   \
        #             5   6

