# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s = [root]
        q = [subRoot]

        while len(s) > 0:
            curr = s.pop()

            if curr != None:
                
                if curr.val == subRoot.val:
                    s2 = [curr]
                    res = True
                    while (len(s2) > 0 and len(q) > 0) and res:
                        curr1 = s2.pop()
                        curr2 = q.pop()

                        if not curr1 and curr2:
                            res = False
                        
                        if not curr2 and curr1:
                            res = False

                        if curr1 and curr2:
                            if curr1.val != curr2.val:
                                res = False
                            
                            s2.append(curr1.left)
                            s2.append(curr1.right)
                            q.append(curr2.left)
                            q.append(curr2.right)
                    if res:
                        return res
                    q = [subRoot]


                s.append(curr.left)
                s.append(curr.right)
        
        return False
