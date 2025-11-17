class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # warshall-floyd 알고리즘 : 모든 간선에 대하여 다른 간선까지의 최단거리를 구할 수 있음
        dists = [[n] * n for _ in range(n)]
        for i in range(n):
            dists[i][i] = 0
        
        for u, v in edges:
            dists[u-1][v-1] = 1
            dists[v-1][u-1] = 1
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dists[i][j] > dists[i][k] + dists[k][j]:
                        dists[i][j] = dists[i][k] + dists[k][j]
        
        ans = [0] * (n-1)
        # 모든 subtree 경우의 수를 활용하기 위해 mask 사용
        max_mask = 1 << n
        for mask in range(max_mask):
            print(mask)
            # 노드가 0개 or 1개인 경우는 스킵
            if mask & (mask - 1) == 0:
                continue

            max_dist = 0
            edge_count = 0
            city_count = 0

            # 부분집합에 포함된 정점 쌍 (u, v)를 다 봄
            for u in range(n):
                if not (mask & (1 << u)):
                    continue
                city_count += 1
                for v in range(u + 1, n):
                    if not (mask & (1 << v)):
                        continue
                    if dists[u][v] == 1:
                        edge_count += 1
                    # 연결되어 있는 경우에만 max_dist 갱신
                    if dists[u][v] < n:
                        if dists[u][v] > max_dist:
                            max_dist = dists[u][v]
            # 연결성 확인 조건 = edge가 node의 개수보다 하나 적음
            if edge_count == city_count - 1 and max_dist > 0:
                ans[max_dist - 1] += 1

        return ans
        
