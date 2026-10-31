# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        for i, n in enumerate(inorder):
            indices[n] = i

        self.pre_index = 0
        def dfs(l, r):
            if l > r:
                return None
            
            root_val = preorder[self.pre_index]
            self.pre_index += 1


            m = indices[root_val]
            
            return TreeNode(root_val, dfs(l, m - 1), dfs(m + 1, r))

        return dfs(0, len(inorder) - 1)

        



            
