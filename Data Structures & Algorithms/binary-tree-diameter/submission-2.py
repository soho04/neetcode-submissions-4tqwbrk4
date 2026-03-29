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

            print(node.val)

            maxHeight = max(dfs(node.left), dfs(node.right))
            maxDia = dfs(node.left) + dfs(node.right)

            maximumHeightorDia = max(maxHeight, maxDia)

            self.maxDia = max(self.maxDia, maximumHeightorDia)

            return 1 + max(dfs(node.left), dfs(node.right))

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

