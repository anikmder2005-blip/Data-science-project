class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            adj[src].append(dest)
        state = [0] * numCourses
        def has_cycle(node):
            if state[node] == 1: return True
            if state[node] == 2: return False
            state[node] = 1
            for neighbor in adj[node]:
                if has_cycle(neighbor): return True
            state[node] = 2
            return False
        for i in range(numCourses):
            if has_cycle(i): return False
        return True
