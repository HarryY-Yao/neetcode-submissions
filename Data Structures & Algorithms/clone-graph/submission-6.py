"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        root = Node(node.val)
        q = deque([node])

        cloned = {node : root}

        while q:
            curr1 = q.popleft()
            curr2 = cloned[curr1]

            for neighbor in curr1.neighbors:
                if neighbor not in cloned:
                    q.append(neighbor)
                    clone = Node(neighbor.val)
                    cloned[neighbor] = clone
                curr2.neighbors.append(cloned[neighbor])
                
        return root




