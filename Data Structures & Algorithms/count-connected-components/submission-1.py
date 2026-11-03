class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for a, b in edges:
            parent_a = find(a)
            parent_b = find(b)
            if parent_a != parent_b:
                parent[parent_a] = parent_b
        
        return len(set(find(x) for x in range(n)))