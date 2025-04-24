from collections import defaultdict
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = defaultdict(list)
        for [a,b] in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(start,end):
            if start == end:
                return True
            visited.add(start)
            for node in graph[start]:
                if node not in visited:
                    visited.add(node)
                    if dfs(node, end):
                        return True
            return False
        return dfs(source, destination)