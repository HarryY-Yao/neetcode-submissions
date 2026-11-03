class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        visited = {}
        rec_stack = {}

        for prereq in prerequisites:
            crs, pre = prereq
            if crs not in adj:
                adj[crs] = []
            adj[crs].append(pre)
        
        for u in range(numCourses):
            visited[u] = False
            rec_stack[u] = False

        def dfs(adj, u, visited, rec_stack):
            if rec_stack[u]:
                return True

            if visited[u]:
                return False

            visited[u] = True
            rec_stack[u] = True
            for v in adj.get(u, []):
                if dfs(adj, v, visited, rec_stack):
                    return True

            rec_stack[u] = False
            return False

        for u in range(numCourses):
            if not visited[u] and dfs(adj, u, visited, rec_stack):
                return False
        
        return True