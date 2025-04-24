from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)
        results = []
        n = len(equations)
        for i in range(n):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]]=1/values[i]
        def dfs(vertex , ans , target , visited):
            if vertex == str(target):
                return ans
            visited.add(vertex)
            for key in graph[vertex].keys():
                if key in visited:
                    continue
                res = dfs(key,ans * graph[vertex][key],target,visited)
                if res != -1:
                    return res
            return -1
        for a, b in queries:
            if a not in graph or b not in graph:
                results.append(-1.0)
            elif a == b:
                results.append(1.0)
            else:
                results.append(dfs(a, 1.0,b, set()))
        return results
