class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
       
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = set()
        ans = 0

        for node in range(n):
            if node in vis: continue

            q = [node]
            comp = set([node]) # component

            while q:
                tq = [] # temporary queue (to be added in the queue)

                for nei in q: # neighbour nodes
                    vis.add(nei)
                    for connNei in adj[nei]: # connected neighbour nodes
                        if connNei not in vis:
                            tq.append(connNei)
                            comp.add(connNei)

                q = tq # update queue

            conns = len(comp) - 1 # number of connections each node should have
            isConnComp = True

            for i in comp:
                if len(adj[i]) != conns:
                    isConnComp = False
                    break

            if isConnComp:
                ans += 1

        return ans