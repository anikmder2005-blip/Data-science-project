class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build graph and calculate indegree
        for edge in prerequisites:

            course = edge[0]
            prerequisite = edge[1]

            graph[prerequisite].append(course)
            indegree[course] += 1

        que = []

        # Add courses with no prerequisites
        for i in range(numCourses):
            if indegree[i] == 0:
                que.append(i)

        answer = [0] * numCourses
        index = 0
        front = 0

        # Kahn's Algorithm
        while front < len(que):

            curr = que[front]
            front += 1

            answer[index] = curr
            index += 1

            # Process dependent courses
            for neighbor in graph[curr]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    que.append(neighbor)

        # If not all courses were processed, a cycle exists.
        if index != numCourses:
            return []

        return answer