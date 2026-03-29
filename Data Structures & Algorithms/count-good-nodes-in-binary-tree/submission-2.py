# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.count = 0

        def dfs(node, pathMax):

            if not node:
                return

            print(node.val, pathMax)
            if node.val >= pathMax:
                
                pathMax = node.val
                self.count += 1

            dfs(node.left, pathMax)
            dfs(node.right, pathMax)
        
        dfs(root, root.val)

        return self.count

        #               -1
        #

