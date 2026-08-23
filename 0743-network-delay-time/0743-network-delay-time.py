
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjList = []

        # Create adjacency list
        for i in range(n):
            adjList.append([])

        # Add edges
        for edge in times:
            x = edge[0] - 1
            y = edge[1] - 1
            w = edge[2]

            adjList[x].append([y, w])

        # Min heap and distance array
        heap = []
        dist = [float("inf")] * n

        # Starting node
        dist[k - 1] = 0
        heappush(heap, (0, k - 1))

        # Dijkstra's Algorithm
        while len(heap) > 0:
            d, u = heappop(heap)

            # Skip old entries
            if d > dist[u]:
                continue

            for v, w in adjList[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heappush(heap, (dist[v], v))

        ans = max(dist)

        if ans == float("inf"):
            return -1

        return ans