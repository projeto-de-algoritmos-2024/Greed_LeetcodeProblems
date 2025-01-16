# Questão Difícil 1090. Largest Values From Labels - Algoritmo de Kruskal
class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(edges)):
            edges[i].append(i)
        
        edges.sort(key=lambda x: x[2])

        def kruskal(n, edges, skip_edge=-1, force_edge=-1):
            parent = list(range(n))
            rank = [0] * n

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(x, y):
                rootX = find(x)
                rootY = find(y)
                if rootX != rootY:
                    if rank[rootX] > rank[rootY]:
                        parent[rootY] = rootX
                    elif rank[rootX] < rank[rootY]:
                        parent[rootX] = rootY
                    else:
                        parent[rootY] = rootX
                        rank[rootX] += 1

            mst_weight = 0
            edges_used = 0

            if force_edge != -1:
                u, v, w, _ = edges[force_edge]
                union(u, v)
                mst_weight += w
                edges_used += 1

            for i, (u, v, w, idx) in enumerate(edges):
                if i == skip_edge:
                    continue
                if find(u) != find(v):
                    union(u, v)
                    mst_weight += w
                    edges_used += 1

            return mst_weight if edges_used == n - 1 else float('inf')

        original_mst_weight = kruskal(n, edges)

        critical = []
        pseudo_critical = []

        for i in range(len(edges)):
            if kruskal(n, edges, skip_edge=i) > original_mst_weight:
                critical.append(edges[i][3])
            elif kruskal(n, edges, force_edge=i) == original_mst_weight:
                pseudo_critical.append(edges[i][3])

        return [critical, pseudo_critical]

solution = Solution()

n1 = 5
edges1 = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]
print("Output Exemplo 1:", solution.findCriticalAndPseudoCriticalEdges(n1, edges1))

n2 = 4
edges2 = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]
print("Output Exemplo 2:", solution.findCriticalAndPseudoCriticalEdges(n2, edges2))