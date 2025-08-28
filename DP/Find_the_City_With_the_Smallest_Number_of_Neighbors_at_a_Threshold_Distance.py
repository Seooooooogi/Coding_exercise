class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = float('inf')
        min_neighbors = n
        dist = [[INF] * n for _ in range(n)]

        # Floyd-warshall 알고리즘
        for u in range(n):
            dist[u][u] = 0
        
        # 양방향이기 때문에 초기화에 주의
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # k를 가장 바깥 정점에 두어야 함
        # k=0(0번 노드만) 부터 k=n(모든 정점 사용 가능)을 통해 i와 j 사이의 최단거리를 갱신
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] <= dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        for i in range(n):
            neighbors = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold and i != j:
                    neighbors += 1

            if neighbors <= min_neighbors:
                answer = i
                min_neighbors = neighbors

        return answer
        
