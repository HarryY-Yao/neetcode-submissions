# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        s = [root]
        res = root
        
        while len(s) > 0:
            curr = s.pop()

            if curr != None:
                if curr.val in [p.val, q.val]:
                    return curr
                
                if p.val < curr.val < q.val or p.val > curr.val > q.val:
                    return curr

                if curr.val > p.val and curr.val > q.val:
                    s.append(curr.left)

                else:
                    s.append(curr.right)

        return res



        
