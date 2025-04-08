from collections import defaultdict
import heapq

def solution(N, road, K):
    answer = 0
    INF = 10 ** 10
    graph = defaultdict(list)
    
    # 양방향으로 노드를 생성해주어야 순회가 가능함
    for src_node, tgt_node, weight in road:
        graph[src_node-1].append((tgt_node-1, weight))
        graph[tgt_node-1].append((src_node-1, weight))
    
    distances = [INF] * N
    distances[0] = 0
    visited = [False] * N
    
    q = [(0, 0)]
    
    # 음의 가중치가 없으므로 다익스트라 알고리즘 사용
    while q:
        cur_distance, cur_node = heapq.heappop(q)
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        for next_node, weight in graph[cur_node]:
            new_distance = distances[cur_node] + weight
            if new_distance < distances[next_node]:
                distances[next_node] = new_distance
                heapq.heappush(q, (new_distance, next_node))
    
    # 목표 시간보다 낮은 곳을 체크      
    return sum(1 for d in distances if d <= K)
  
