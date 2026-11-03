class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        visited = {}
        res = True
        
        for node in range(n):
            adj[node] = []
            visited[node] = False

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def bfs(u, visited):

            q = deque([u])
            visited[u[0]] = True

            while q:
                curr, parent = q.popleft()

                for child in adj[curr]:
                    if not visited[child]:
                        visited[child] = True
                        q.append((child, curr))
                    elif visited[child] and child != parent:
                        return False
            
            return True

        no_cycle = bfs((0, -1), visited)

        for node in visited.keys():
            res = res and visited[node]
        
        return no_cycle and res

                    

