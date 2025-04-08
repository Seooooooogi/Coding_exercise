# 정점의 개수-1만큼 비용을 반복 갱신
# 시간복잡도 : O(VxE), V: 정점 수, E: 간선 수
def bellman_ford(source, num_vertices, edges):
    INF = 10 ** 10
    graph = [[] for _ in range(num_vertices)]
    for edge in edges:
        src_vertex, tgt_vertex, weight = edge
        graph[src_vertex].append((tgt_vertex, weight))
    distances = [INF] * num_vertices
    distances[source] = 0

    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            for v, w in graph[u]:
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

    # 음의 순환 확인
    # 새롭게 갱신이 일어난다 = 음의 순환이 존재한다
    for u in range(num_vertices):
        for v, w in graph[u]:
            if distances[u] + w < distances[v]:
                return [-1]

    return distances
  
