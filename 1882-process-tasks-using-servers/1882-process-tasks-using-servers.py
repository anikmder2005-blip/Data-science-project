class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [[w, s] for s, w in enumerate(servers)]
        heapify(available)
        using = []
        n = len(tasks)

        res = []
        for i in range(n):
            while using and using[0][0] <= i:
                et, w, s = heappop(using)
                heappush(available, [w, s])
            if available:
                w, s = heappop(available)
                heappush(using, [i + tasks[i], w, s])
            else:
                et, w, s =heappop(using)
                heappush(using, [et + tasks[i], w, s])
            res.append(s)
        return res