import heapq
from collections import defaultdict

INF = 10 ** 10

# 그리디한 풀이방법
def daijkstra(start, num_nodes, edges):
    graph = defaultdict(list)
    for cur_node, next_node, weight in edges:
        graph[cur_node].append((next_node, weight))
    
    distances = [INF] * num_nodes
    # 모든 정점을 단 한번만 방문함
    visited = [False] * num_nodes
    distances[start] = 0
    
    q = [(0, start)]

    while q:
        # 우선순위 큐를 활용하여 효율적으로 풀이
        cur_distance, cur_node = heapq.heappop(q)

        if visited[cur_node]:
            continue
    
        visited[cur_node] = True
    
        for next_node, weight in graph[cur_node]:
            new_distance = cur_distance + weight
            if new_distance < distances[next_node]:
                distances[next_node] = new_distance
                heapq.heappush(q, (new_distance, next_node))

    return distances
    
